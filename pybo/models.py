from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, nullable=True)
    rack = db.Column(db.Integer, nullable=True)
    v37 = db.Column(db.Integer, nullable=True)
    v74 = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lon = db.Column(db.Float, nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, nullable=True)
    rack = db.Column(db.Integer, nullable=True)
    v37 = db.Column(db.Integer, nullable=True)
    v74 = db.Column(db.Integer, nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)
