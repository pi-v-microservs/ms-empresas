from flask import Blueprint, request

from data.database import db
from domain.models.Vaga import Vaga

bp = Blueprint('vagas_controllers', __name__, url_prefix='/vagas')


@bp.route('/list', methods=['GET'])
def list_vagas_empresa():
    try:
        return {'vagas': [
            vaga.to_dict() for vaga in (Vaga
                                        .query
                                        .filter_by(id_empresa=request.args.get('id_empresa'))
                                        .all())]}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/get', methods=['GET'])
def get_vaga():
    try:
        return (Vaga
                .query
                .filter_by(id_vaga=request.args.get('id_vaga'))
                .first()
                .to_dict())
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/create', methods=['POST'])
def create_vaga():
    try:
        vaga_criar = Vaga(**request.form)
        db.session.add(vaga_criar)
        db.session.commit()
        return {'message': 'vaga criada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/update', methods=['PUT'])
def update_vaga():
    try:
        vaga_atualizar = (Vaga
                          .query
                          .filter_by(id_vaga=request.form.get('id_vaga'))
                          .first())

        vaga_atualizar.titulo = request.form.get('titulo')
        vaga_atualizar.cargo = request.form.get('cargo')
        vaga_atualizar.descricao = request.form.get('descricao')
        vaga_atualizar.data_abertura = request.form.get('data_abertura')
        vaga_atualizar.data_fechamento = request.form.get('data_fechamento')

        db.session.commit()
        return {'message': 'vaga atualizada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/delete', methods=['DELETE'])
def delete_vaga_profissional():
    try:
        vaga_deletar = Vaga.query.filter_by(id_vaga=request.form.get('id_vaga')).first()

        db.session.delete(vaga_deletar)
        db.session.commit()
        return {'message': 'vaga deletada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}
