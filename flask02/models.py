from app import db

def sec():
    return db.Table('Telefono_Propietario',
    db.Column('telefono_id',db.Integer,db.ForeignKey('telefono.id')),
    db.Column('propietario_id',db.Integer,db.ForeignKey('propietario.id')))

class Telefono(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True)
    model = db.Column(db.String(80),unique=True)
    owners = db.relationship('Propietario',secondary=sec(),backref=db.backref('telefonos',lazy='dynamic'))

    def __repr__(self):
        return f"<Telefono {self.name}>"

class Propietario(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(70),unique=True)

    def __repr__(self):
        return "<Propietario %s>"%(self.fullname)