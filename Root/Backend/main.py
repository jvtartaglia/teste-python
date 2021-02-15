from app import app, db
from models import *
from sql_query import parent_sql_query, child_sql_query
from flask import render_template, request, Response
import json


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static')
def static_page():
    return render_template('static.html')


@app.route('/api/parent', methods = ['POST'])
def create_parent():
    body = request.get_json()
    try:
        parent = Parent(name = body['name'], email = body['email'])
        db.session.add(parent)
        
        if 'child_id' in body:
            try:
                for id in body['child_id']:
                    child_object = Child.query.filter_by(id = id).first()
                    parent.children.append(child_object)
            except Exception as e:
                print(e)
                return Response("{'Bad request':'could not match child_id}", status = 400, mimetype = 'application/json')

        db.session.commit()
        return Response("{'Ok':'parent created sucessfully'}", status = 201, mimetype = 'application/json')
    except Exception as e:
        print(e)
        return Response("{'Bad request':'parent not created'}", status = 400, mimetype = 'application/json')
    
    
@app.route('/api/child', methods = ['POST'])
def create_child():
    body = request.get_json()
    try:
        child = Child(name = body['name'], email = body['email'])
        db.session.add(child)
        
        if 'parent_id' in body:
            if len(body['parent_id']) > 2:
                return Response("{'Bad request':'child can have maximum 2 parents'}", status = 400, mimetype = 'application/json')
            else:
                try:
                    for id in body['parent_id']:
                        parent_object = Parent.query.filter_by(id = id).first()
                        child.parents.append(parent_object)
                except Exception as e:
                    print(e)
                    return Response("{'Bad request':'could not match parent_id}", status = 400, mimetype = 'application/json')

        db.session.commit()
        return Response("{'Ok':'child created sucessfully'}", status = 201, mimetype = 'application/json')
    except Exception as e:
        print(e)
        return Response("{'Bad request':'child not created'}", status = 400, mimetype = 'application/json')
        

@app.route('/api/parent/<id>', methods = ['GET'])
def get_parent(id):
    parent_object = Parent.query.filter_by(id = id).first()
    parent_id_json = parent_object.to_json()
    return Response(json.dumps(parent_id_json, default = str, indent = 4), status = 200)


@app.route('/api/child/<id>', methods = ['GET'])
def get_child(id):
    child_object = Child.query.filter_by(id = id).first()
    child_id_json = child_object.to_json()
    return Response(json.dumps(child_id_json, default = str, indent = 4), status = 200)


@app.route('/api/parent/<id>', methods = ['PUT'])
def update_parent(id):
    parent_object = Parent.query.filter_by(id = id).first()
    body = request.get_json()
    try:
        if 'name' in body:
            parent_object.name = body['name']
        if 'email' in body:
            parent_object.email = body['email']

        db.session.add(parent_object)
        db.session.commit()
        return Response("{'Ok':'parent updated sucessfully'}", status = 200, mimetype = 'application/json')
    
    except Exception as e:
        print(e)
        return Response("{'Bad request':'parent not updated'}", status = 400, mimetype = 'application/json')


@app.route('/api/child/<id>', methods = ['PUT'])
def update_child(id):
    child_object = Child.query.filter_by(id = id).first()
    body = request.get_json()
    try:
        if 'name' in body:
            child_object.name = body['name']
        if 'email' in body:
            child_object.email = body['email']
            
        db.session.add(child_object)
        db.session.commit()
        return Response("{'Ok':'child updated sucessfully'}", status = 200, mimetype = 'application/json')
    
    except Exception as e:
        print(e)
        return Response("{'Bad request':'child not updated'}", status = 400, mimetype = 'application/json')


@app.route('/api/parent/<id>', methods = ['DELETE'])
def delete_parent(id):
    parent_object = Parent.query.filter_by(id = id).first()
    try:
        db.session.delete(parent_object)
        db.session.commit()
        return Response("{'Ok':'parent deleted sucessfully'}", status = 200, mimetype = 'application/json') 
    except Exception as e:
        print(e)
        return Response("{'Bad request':'parent could not be deleted'}", status = 400, mimetype = 'application/json')


@app.route('/api/child/<id>', methods = ['DELETE'])
def delete_child(id):
    child_object = Child.query.filter_by(id = id).first()
    try:
        db.session.delete(child_object)
        db.session.commit()
        return Response("{'Ok':'child deleted sucessfully'}", status = 200, mimetype = 'application/json') 
    except Exception as e:
        print(e)
        return Response("{'Bad request':'child could not be deleted'}", status = 400, mimetype = 'application/json')


@app.route('/api/parents', methods = ['GET'])
def get_parents():
    parents_object = Parent.query.all()
    parents_json = [parent.to_json() for parent in parents_object]
    return Response(json.dumps(parents_json, default = str, indent = 4), status = 200)


@app.route('/api/children', methods = ['GET'])
def get_children():
    children_object = Child.query.all()
    children_json = [child.to_json() for child in children_object]
    return Response(json.dumps(children_json, default = str, indent = 4), status = 200)

# TODO
# testar mesma rota com e sem argumento
# contar ocorrencias no bd

@app.route('/parents', methods = ['GET'])
def get_parents_count():
    count = request.args['children']
    query_result = db.engine.execute(parent_sql_query(count))
    print(query_result)
    # parents_object = Parent.query.filter_by(count = count)
    # parents_json = [parent.to_json() for parent in parents_object]
    # return Response(json.dumps(parents_json, default = str, indent = 4))
    
    
# @app.route('/children', methods = ['GET'])
# def get_children_count():
#     count = request.args['parents']
#     children_object = Child.query.filter_by(count = count)
#     children_json = [child.to_json() for child in children_object]
#     return Response(json.dumps(children_json, default = str, indent = 4))


if __name__ == '__main__':
    app.run(debug=True)