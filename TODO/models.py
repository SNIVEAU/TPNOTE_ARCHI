import base64
from sqlalchemy import LargeBinary
from flask_login import UserMixin
from .app import db, login_manager
from datetime import *

tasks = [
    {
        'id': 1,
        'title': 'Courses ',
        'description': 'Salade , Oignons , Pommes , Clementines ',
        'done': True
    },
    {
        'id': 2,
        'title': 'Apprendre REST ',
        'description': 'Apprendre mon cours et comprendre les exemples ',
        'done': False
    },
    {
        'id': 3,
        'title': 'Apprendre Ajax ',
        'description': 'Revoir les exemples et ecrire un client REST JS avec Ajax ',
        'done': False
    }
]
class Questionnaire (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String (100))
    def __init__ (self , name):
        self.name = name
    def __repr__ (self):
        return "<Questionnaire (%d) %s>" % (self.id , self.name)
    def to_json (self):
        json = {}
        for question in self.questions:

            json ={
            'id': self.id ,
            'name ':self.name ,
            'questions':[q.to_json() for q in self.questions]}
        return json
    def __init__(self,name):
        self.id = len(Questionnaire.query.all())+1
        self.name = name
def get_all_questions(id_questionnaire):
    return db.Query.filter(id_questionnaire)
class Question (db.Model):
    id = db.Column(db.Integer,primary_key = True)
    __mapper_args__ = {
        'polymorphic_identity':'question',
        'polymorphic_on': 'questionType'
    }
    title = db.Column(db.String (120))
    reponse = db.Column(db.String(120))
    questionType = db.Column(db.String (120))
    questionnaire_id = db.Column(db.Integer,db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship ("Questionnaire", backref = db.backref("questions",lazy="dynamic"))
    def to_json(self):
        json = {
            'id': self.id ,
        'title ':self.title ,
        'reponse':self.reponse,
        'questionType':self.questionType,

        }
        return json
    def __init__(self,title,reponse,questionType,questionnaire):
        self.id = len(Question.query.get())+1
        self.title = title
        self.reponse = reponse
        self.questionType = questionType
        self.questionnaire_id = questionnaire
        db.session.add(self)
        db.session.commit()
    def __init__(self,request,id):
        self.id = len(Question.query.all())+1
        self.title = request['title']
        self.reponse = request['reponse']
        self.questionType = request['questionType']
        self.questionnaire_id = id
        db.session.add(self)
        db.session.commit

class QuestionSimple(Question):
    __mapper_args__ = {
        'polymorphic_identity':'Simple'
    }
    id = db.Column(db.Integer,db.ForeignKey('question.id'),primary_key = True)
    p1 = db.Column(db.Integer)
    p2 = db.Column(db.Integer)
    reponse = db.Column(db.String(120))
    questionType = db.Column(db.String (120))
    def __init__(self,title,reponse,questionnaire,p1='',p2=''):
        self.id = len(Question.query.all())+1
        self.title = title
        self.p1=p1
        self.p2=p2
        self.reponse = reponse
        self.questionType = 'Simple'
        self.questionnaire_id = questionnaire
        db.session.add(self)
        db.session.commit()
    def __init__(self,request,id):
        self.id = len(Question.query.all())+1
        self.title = request['title']
        self.reponse = request['reponse']
        self.questionType = 'Simple'
        self.questionnaire_id = id
        self.p1 = request['p1']
        self.p2 = request['p2']
        db.session.add(self)
        db.session.commit()
    def to_json(self):
        json = {
            'id': self.id ,
        'title ':self.title ,
        'reponse':self.reponse,
        'questionType':self.questionType,
        'p1':self.p1,
        'p2':self.p2,
        }
        return json
class QuestionMultiple(Question):
    __mapper_args__ = {
        'polymorphic_identity':'Multiple'
    }
    id = db.Column(db.Integer,db.ForeignKey('question.id'),primary_key = True)
    p1 = db.Column(db.Integer)
    p2 = db.Column(db.Integer)
    p3 = db.Column(db.Integer)
    p4 = db.Column(db.Integer)

    reponse = db.Column(db.String(120))
    questionType = db.Column(db.String (120))
    def save_bd(self):
        db.session.add(self)
        db.session.commit()
    def __init__(self,title,reponse,questionnaire,p1='',p2='',p3='',p4=''):
        self.id = len(Question.query.all())+1
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.title = title
        self.reponse = reponse
        self.questionType = 'Multiple'
        self.questionnaire_id = questionnaire
        db.session.add(self)
        db.session.commit()
    def __init__(self,request,id):
        self.id = len(Question.query.all())+1
        self.title = request['title']
        self.p1 = request['p1']
        self.p2 = request['p2']
        self.p3 = request['p3']
        self.p4 = request['p4']
        self.reponse = request['reponse']
        self.questionType = 'Multiple'
        self.questionnaire_id = id
        db.session.add(self)
        db.session.commit()
    def to_json(self):
        json = {
            'id': self.id ,
        'title ':self.title ,
        'reponse':self.reponse,
        'questionType':self.questionType,
        'p1':self.p1,
        'p2':self.p2,
        'p3':self.p3,
        'p4':self.p4,
        }
        return json