from typing import List

from data.database import db
from domain.models import Vaga


class Empresa(db.Model):
    __tablename__ = 'empresas'
    id_empresa = db.Column('id_empresa', db.Integer, primary_key=True)
    nome = db.Column('nome', db.VARCHAR)
    cnpj = db.Column('cnpj', db.VARCHAR)
    setor = db.Column('setor', db.UnicodeText)

    vagas: List[Vaga] = db.relationship('Vaga', backref='empresa')

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not (key.startswith('_'))}
