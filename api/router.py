from flask import Blueprint, request
from database.main import Caminho, Ponto, dict_to_ponto, list_all

router = Blueprint('router', __name__,)


@router.route('/novo', methods=['POST'])
def create_new():
	pontos = [dict_to_ponto(ponto) for ponto in request.json['pontos']]
	caminho = Caminho(pontos)
	caminho.insert()
	return { 'error': False, 'caminho': caminho.to_json() }

@router.route('/atualizar/<int:id>', methods=['PUT'])
def update(id):
	pontos = [dict_to_ponto(ponto) for ponto in request.json['pontos']]
	caminho = Caminho(pontos, id)
	caminho.update()
	return { 'error': False, 'caminho': caminho.to_json() }

@router.route('/pegar_caminho/<int:id>')
def get_one(id):
	caminho = Caminho().get(int(id))
	if caminho == None: return { 'error': True, 'message': 'Caminho não encontrado' }

	return { 'error': False, 'caminho': caminho.to_json() }

@router.route('/listar_caminhos')
def get_all():
	caminhos = list_all()
	print(caminhos)
	caminhos_obj = []
	for caminho in caminhos:
		id = str(list(caminho.keys())[0]).replace('caminho_', '')
		pontos = [dict_to_ponto(ponto) for ponto in caminho[list(caminho.keys())[0]]]
		caminhos_obj.append(Caminho(pontos, id).to_json())

	print(caminhos_obj)
	return { 'error': False, 'caminhos': caminhos_obj }

@router.route('/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
	Caminho().remove(id)
	return { 'error': False }