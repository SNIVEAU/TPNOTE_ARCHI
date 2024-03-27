from flask import jsonify , abort , make_response , request,url_for
from .app import app
from .models import *
def make_public_task (task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri']=url_for('get_task',task_id = task['id'],_external = True)
        else:
            new_task[field] = task[field]
    return new_task
@app.route('/quiz/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify (tasks =[ make_public_task (t) for t in tasks ])


@app.route('/quiz/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort (400)
    task = {
        'id': tasks [-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify ( { 'task ': make_public_task (task) } ), 201

@app.route('/quiz/api/v1.0/tasks/<int:task_id>')
def get_task(task_id):
    task = [task for task in tasks if task['id']==task_id]
    if len(task)>task_id:
        abort(404)
    return jsonify (task[0])

@app.route('/quiz/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort (400)
    if 'description' in request.json and type(request.json['description']) != str:
        abort (400) 
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort (400)
    task[0]['title'] = request.json.get('title',task[0]['title'])
    task[0]['description'] = request .json.get('description', task[0]['description'])
    task[0]['done'] = request .json.get('done ', task[0]['done'])
    return jsonify({'task':make_public_task(task[0])})

@app.route('/quiz/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    tasks.remove(task[0])
    return jsonify ({'result': True})

@app.errorhandler(404)
def not_found (error):
    return make_response(jsonify({ 'error': 'Not found'}),404)

@app.errorhandler(400)
def not_found (error):
    return make_response(jsonify({'error': 'Bad request'}),400)

@app.route('/quiz/api/v2.0/questionnaires', methods = ['GET'])
def get_questionnaires():
    return jsonify (questionnaires =[q.to_json() for q in Questionnaire.query.all() ])

@app.route('/quiz/api/v2.0/questionnaires/<int:questionnaire_id>', methods = ['GET'])
def get_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if not questionnaire:
        abort(404)
    return jsonify (questionnaire.to_json())
@app.route('/quiz/api/v2.0/questionnaires', methods = ['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort (400)
    questionnaire = Questionnaire(request.json['name'])
    db.session.add(questionnaire)
    db.session.commit()
    return jsonify (questionnaire.to_json()), 201
@app.route('/quiz/api/v2.0/questionnaires/<int:questionnaire_id>', methods = ['PUT'])
def update_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if not questionnaire:
        abort(404)
    if not request.json:
        abort(400)
    
    questionnaire.name = request.json.get('name',questionnaire.name)
    db.session.commit()
    return jsonify (questionnaire.to_json())
@app.route('/quiz/api/v2.0/questionnaires/<int:questionnaire_id>', methods = ['DELETE'])
def delete_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if not questionnaire:
        abort(404)
    db.session.delete(questionnaire)
    db.session.commit()
    return jsonify ({'result': True})
@app.route('/quiz/apiv2.0/questions', methods = ['GET'])
def get_questions():
    return jsonify (questions =[q.to_json() for q in Question.query.all()])
@app.route('/quiz/apiv2.0/questions/<int:questionnaire_id>',methods = ['POST'])
def add_questions(questionnaire_id):
    if not request.json or not 'title' in request.json:
        abort(400)
    question = Question(request.json,questionnaire_id)

    return jsonify (question.to_json()), 201

    
@app.route('/quiz/apiv2.0/questions', methods = ['POST'])
def create_question():
    print(request.json)
    print(request.json['title'])
    if not request.json or not 'title' in request.json or not 'questionType' in request.json or not 'questionnaire_id' in request.json:
        abort (400)
    if request.json['questionType'] == "simple":
        question = QuestionSimple(request.json,request.json['questionnaire_id'])
    elif request.json['questionType'] == "multiple":
        # question = QuestionMultiple(request.json['title']
        #                             ,request.json['reponse']
        #                             ,request.json['questionnaire_id']
        #                             ,request.json['p1'],request.json['p2']
        #                             ,request.json['p3'],request.json['p4'])
        question = QuestionMultiple(request.json,request.json['questionnaire_id'])
        
    else:
        return None
    return jsonify (question.to_json()), 201