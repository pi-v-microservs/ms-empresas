from flask import Blueprint, request

from data.database import db
from domain.models.Empresa import Empresa

bp = Blueprint('empresas_controllers', __name__, url_prefix='/empresas')


@bp.route('/list', methods=['GET'])
def list_empresas():
    try:
        return {'empresas': [empresa.to_dict() for empresa in Empresa.query.all()]}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/get', methods=['GET'])
def get_empresa():
    try:
        return Empresa.query.filter_by(id_empresa=request.args.get('id_empresa')).first().to_dict()
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/create', methods=['POST'])
def create_empresa():
    try:
        empresa_criar = Empresa(**request.form)
        db.session.add(empresa_criar)
        db.session.commit()
        return {'message': 'empresa criada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/update', methods=['PUT'])
def update_empresa():
    try:
        empresa_atualizar = Empresa.query.filter_by(id_empresa=request.form.get('id_empresa')).first()

        empresa_atualizar.nome = request.form.get('nome')
        empresa_atualizar.cnpj = request.form.get('cnpj')
        empresa_atualizar.setor = request.form.get('setor')

        db.session.commit()
        return {'message': 'empresa atualizado com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/delete', methods=['DELETE'])
def delete_empresa():
    try:
        empresa_deletar = Empresa.query.filter_by(id_empresa=request.form.get('id_empresa')).first()

        db.session.delete(empresa_deletar)
        db.session.commit()
        return {'message': 'empresa deletada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}
