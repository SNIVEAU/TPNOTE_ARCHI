import click
from .app import app,db
from .models import *
from datetime import *
from hashlib import sha256

@app.cli.command()
def destroydb():
    """Destruction de toutes les tables."""
    db.drop_all()

@app.cli.command()
def syncdb():
    """Création de toutes les tables."""
    db.create_all()

@app.cli.command()
def resetdb():
    """Destruction et recréation de toutes les tables."""
    db.drop_all()
    db.create_all()
@app.cli.command()
def creaQuestion():
    """Création des questions."""
    db.drop_all()
    db.create_all()
    q = Questionnaire("Questionnaire 1")
    db.session.add(q)
    db.session.commit()
    # q1 = Question(id=1,
    #         title="Question 1",
    #         reponse="crampte",
    #         questionType="",
    #         questionnaire_id=1)
    # q2 = Question(id=2,
    #         title="Question 2",
    #         reponse="crampte",
    #         questionType="text",
    #         questionnaire_id=1)
    # q3 = Question(id=3,
    #         title="Question 3",
    #         reponse="crampte",
    #         questionType="text",
    #         questionnaire_id=1)  
    q1 = QuestionSimple("Question 1","crampte",1,'crampte','non') 
    q2 = QuestionSimple("Question 2","crampte",1,'crampte','oui')
    q3 = QuestionMultiple("Question 3","oui",1,'non','oui','nooo','ouais')     

    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.commit()
    print("Questionnaire créé avec succès")
