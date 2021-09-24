from data.database import db


class VagaCandidato(db.Model):
    __tablename__ = 'vagas_candidatos'
    id_vaga_candidato = db.Column('id_vaga_candidato', db.Integer, primary_key=True)
    id_vaga = db.Column(db.Integer, db.ForeignKey('vagas.id_vaga'))
    id_candidato = db.Column(db.Integer)
    esta_ativo = db.Column(db.Boolean)

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
