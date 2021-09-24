from flask import Blueprint, request

from data.database import db
from domain.models.VagaCandidato import VagaCandidato

bp = Blueprint('vagas_candidatos_controllers', __name__, url_prefix='/vagas_candidatos')


@bp.route('/list', methods=['GET'])
def list_vagas_candidatos_vaga():
    try:
        return {'vagas_candidatos': [
            vaga_candidato.to_dict() for vaga_candidato in (VagaCandidato
                                                            .query
                                                            .filter_by(id_vaga=request.args.get('id_vaga'))
                                                            .all())]}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/get', methods=['GET'])
def get_vaga_candidato():
    try:
        return (VagaCandidato
                .query
                .filter_by(id_vaga_candidato=request.args.get('id_vaga_candidato'))
                .first()
                .to_dict())
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/create', methods=['POST'])
def create_vaga_candidato():
    try:
        vaga_candidato_criar = VagaCandidato(**request.form)
        db.session.add(vaga_candidato_criar)
        db.session.commit()
        return {'message': 'vaga candidato criada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/update', methods=['PUT'])
def update_vaga_candidato():
    try:
        vaga_candidato_atualizar = VagaCandidato.query.filter_by(
            id_curriculo=request.form.get('id_vaga_candidato')).first()

        vaga_candidato_atualizar.id_vaga = request.form.get('id_vaga')
        vaga_candidato_atualizar.id_candidato = request.form.get('id_candidato')
        vaga_candidato_atualizar.esta_ativo = bool(request.form.get('esta_ativo'))

        db.session.commit()
        return {'message': 'vaga candidato atualizada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/delete', methods=['DELETE'])
def delete_vaga_candidato():
    try:
        vaga_candidato_deletar = VagaCandidato.query.filter_by(
            id_vaga_candidato=request.form.get('id_vaga_candidato')).first()

        db.session.delete(vaga_candidato_deletar)
        db.session.commit()
        return {'message': 'curriculo deletado com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}
