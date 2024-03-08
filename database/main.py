from tinydb import TinyDB, Query
import json

db = TinyDB('caminhos.json')

class Ponto:
	def __init__(self, x: float, y: float, z: float, r: float):
		self.x = x
		self.y = y
		self.z = z
		self.r = r

	def to_json(self):
		return self.__dict__


class Caminho:
	def __init__(self, pontos: list[Ponto] = [], id: int | None = None):
		self.pontos = pontos
		if id == None: self.id = len(db.all()) + 1
		else: self.id = id

	def insert(self):
		db.insert({ f'caminho_{self.id}': [ponto.to_json() for ponto in self.pontos] })
		return self.id

	def get(self, id: int):
		result = db.get(doc_id=id)
		if result is None: return None
		self.pontos = [dict_to_ponto(point) for point in result[f'caminho_{id}']]
		self.id = id
		return self

	def update(self):
		db.update({ f'caminho_{self.id}': [ponto.to_json() for ponto in self.pontos] })

	def remove(self, id: int):
		db.remove(doc_ids=[id])

	def to_json(self):
		obj = self
		obj.pontos = [ponto.__dict__ for ponto in obj.pontos]
		return obj.__dict__

def list_all():
	return db.all()

def dict_to_ponto(ponto: dict) -> Ponto:
		return Ponto(ponto['x'], ponto['y'], ponto['z'], ponto['r'])

#! Testes:
# ponto_1 = Ponto(1.0, 2.0, 3.0, 4.0)
# ponto_2 = Ponto(4.0, 3.0, 2.0, 1.0)
# caminho = Caminho([ponto_1, ponto_2])
# caminho.insert()
# print(caminho.to_json())
# # el = db.all()
# print(el[0].doc_id)
