from data.database import db


class Vaga(db.Model):
    __tablename__ = 'vagas'
    id_vaga = db.Column('id_vaga', db.Integer, primary_key=True)
    titulo = db.Column('titulo', db.VARCHAR)
    cargo = db.Column('cargo', db.VARCHAR)
    descricao = db.Column('descricao', db.TEXT)
    data_abertura = db.Column('data_abertura', db.Date)
    data_fechamento = db.Column('data_fechamento', db.Date)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id_empresa'))

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
