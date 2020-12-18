#let's create a simple web application, which we will put in a file called app.py
#Using the base Flask application we are now ready to implement the first entry point of our web service
#created a memory database of tasks, which is nothing more than a plain and simple array of dictionaries. Each entry in the array has the fields that we defined above for our tasks.
#Search the entire collection
from flask import Flask, jsonify
from flask.helpers import make_response

app = Flask(__name__)

visitors = [
        {
            "id": 1,
            "first_name": "Winifield",            
            "last_name": "Barfoot",
            "email": "wbarfoot0@bloglines.com",
            "gender": "Male",
            "ip_address": "37.93.54.248",
        },

        {
            "id": 2,
            "first_name":"Emlyn",
            "last_name": "Jouandet",
            "email": "ejouandet1@independent.co.uk",
            "gender": "Male",
            "ip_address": "227.60.249.45",
        },

        {
            "id": 3,
            "first_name": "Brana",
            "last_name": "Physic",
            "email": "bphysic2@myspace.com",
            "gender": "Female",
            "ip_address": "0.90.227.145",
        },

        {
            "id": 4,
            "first_name": "Alfy",
            "last_name": "Scholtz",
            "email": "ascholtz3@nature.com",
            "gender": "Female",
            "ip_address": "241.193.98.45",
        },

         {
            "id": 5,
            "first_name": "Tracy",
            "last_name": "Coggin",
            "email": "tcoggin4@mapy.cz",
            "gender": "Male",
            "ip_address": "147.201.35.30",
        },

         {
            "id": 6,
            "first_name": "Laney",
            "last_name": "Deme",
            "email": "ldeme5@umn.edu",
            "gender": "Male",
            "ip_address": "112.88.98.164",
        },

         {
            "id": 7,
            "first_name": "Ashlie",
            "last_name": "Le Estut",
            "email": "aleestut6@nationalgeographic.com",
            "gender": "Female",
            "ip_address": "48.51.98.194",
        },

         {
            "id": 8,
            "first_name": "Gerard",
            "last_name": "Ludy",
            "email": "gludy7@qq.com",
            "gender": "Male",
            "ip_address": "127.119.96.228",
        },

         {
            "id": 9,
            "first_name": "Gawain",
            "last_name": "Fenne",
            "email": "gfenne8@google.es",
            "gender": "Male",
            "ip_address": "244.31.100.124",
        },

         {
            "id": 10,
            "first_name": "Olenka",
            "last_name": "Stroulger",
            "email": "ostroulger9@mlb.com",
            "gender": "Female",
            "ip_address": "107.139.233.217",
        }
            
            ]    
# the first version of the GET method
@app.route('/idara/api/v1.0/visitors', methods=['GET'])
def get_visitors():
        return jsonify({'visitors': visitors})

        if __name__ == '__main__':
            app.run(debug=True)

#Now let's write the second version of the GET method for our tasks resource. If you look at the table above this will be the one that is used to return the data of a single task:
#ere we get the id of the task in the URL, and Flask translates it into the task_id argument that we receive in the function.
from flask import abort
@app.route('/idara/api/v1.0/visitors/<int:visitor_id>', methods=['GET'])
def get_visitor(visitor_id):
    visitor = [visitor for visitor  in visitors if visitor['id'] == visitor_id]
    if len(visitor) == 0:
        abort(404)
    return jsonify({'visitor': visitor[0]})

from flask  import make_response
@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify ({'error': 'Not found'}), 404)

#the POST method, which we will use to insert a new item in our task database
from flask import request
@app.route('/idara/api/v1.0/visitors', methods=['POST'])
def create_visitor():
    if not request.json or not 'titl' in request.json:
        abort(400)
        visitor = {
            "id": visitors[-1]["id"]+1,
            "first_name": request.json["first_name"],
            "last_name": request.json["last_name"],
            "email": request.json["email"],
            "gender": request.json["gender"],
            "ip_address": request.json["ip_address"],   
        }
        visitors.append(visitor)
        return jsonify({'visitor': visitor}), 201

#the PUT method
@app.route('/idara/api/v1.0/visitors/<int:visitor_id>', methods=['PUT'])
def update_visitor(visitor_id):
        visitor = [visitor for visitor  in visitors if visitor['id'] == visitor_id]
        if len(visitor) == 0:
            abort(404)
        if not request.json:
            abort(404)
        if "first_name" in request.json and type(request.json["first_name"]) != unicode:
            abort(404)
        if "last_name" in request.json and type(request.json["last_name"]) != unicode:
            abort(404)
        if "email" in request.json and type(request.json["email"]) != unicode:
            abort(404)
        if "gender" in request.json and type(request.json["gender"]) != unicode:
            abort(404)
        if "ip_address" in request.json and type(request.json["ip_address"]) != unicode:
            abort(404)
        visitors[0]["first_name"] = request.json.get("first_name", visitor[0]["first_name"])
        visitors[0]["last_name"] = request.json.get("last_name", visitor[0]["last_name"])
        visitors[0]["email"] = request.json.get("email", visitor[0]["email"])
        visitors[0]["gender"] = request.json.get("gender", visitor[0]["gender"])
        visitors[0]["ip_address"] = request.json.get("ip_address", visitor[0]["ip_address"])
        return jsonify({"visitor" : visitor[0]})

#the delete method
@app.route('/idara/api/v1.0/visitors/<int:visitor_id>', mthods=['DELETE'])
def delete_visitor(visitor_id):
        visitor = visitor = [visitor for visitor  in visitors if visitor['id'] == visitor_id]
        if len(visitor) == 0:
            abort(404)
        visitors.remove(visitor[0])
        return jsonify({'result' : True})   
        
#improving the web service interface
#Instead of returning task ids we can return the full URI that controls the task, so that clients get the URIs ready to be used. For this we can write a small helper function that generates a "public" version of a task to send to the client:
#All we are doing here is taking a task from our database and creating a new task that has all the fields except id, which gets replaced with another field called uri, generated with Flask's url_for.
from flask import url_for
def make_public_visitor(visitor):
    new_visitor= {}
    for field in visitor:
        if field == 'id':
            new_visitor['uri'] = url_for('get_visitor', visitor_id=visitor['id'], _external=True)
        else:
            new_visitor[field] = visitor[field]
    return new_visitor 

# When we return the list of tasks we pass them through this function before sending them to the client:
@app.route('/idara/api/v1.0/visitors', methods=['GET'])
def get_visitors():
    return jsonify({'visitors': [make_public_visitor(visitor) for visitor in visitors]})

#We apply this technique to all the other functions and with this we ensure that the client always sees URIs instead of ids.
# GET Method 2
@app.route('/idara/api/v1.0/visitors/<int:visitor_id>', methods=['GET'])
def get_visitors():
    return jsonify({'visitors': [make_public_visitor(visitor) for visitor in visitors]})
#POST Method
@app.route('/idara/api/v1.0/visitors', methods=['POST'])
def create_visitor():
    return jsonify({'visitors': [make_public_visitor(visitor) for visitor in visitors]})
#PUT Method
@app.route('/idara/api/v1.0/visitors/<int:visitor_id>', methods=['PUT'])
def update_visitor(visitor_id):    
    return jsonify({'visitors': [make_public_visitor(visitor) for visitor in visitors]})
#DELETE Method
@app.route('/idara/api/v1.0/visitors/<int:visitor_id>', methods=['PUT'])
def delete_visitor(visitor_id):
    return jsonify({'visitors': [make_public_visitor(visitor) for visitor in visitors]})
