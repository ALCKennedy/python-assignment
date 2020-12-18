from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify

    app = Flask(__name__)

    visitors = [
        {
            'id': 1,
            'first_name': Winifield,            
            'last_name': Barfoot,
            'email': wbarfoot0@bloglines.com,
            'gender': Male,
            'ip_address': 37.93.54.248,
        }

        {
            'id': 2,
            'first_name':Emlyn,
            'last_name': Jouandet,
            'email': ejouandet1@independent.co.uk,
            'gender': Male,
            'ip_address': 227.60.249.45,
        }

        {
            'id': 3,
            'first_name':Brana,
            'last_name': Physic,
            'email': bphysic2@myspace.com,
            'gender':Female,
            'ip_address': 0.90.227.145,
        }

        {
            'id': 4,
            'first_name': Alfy,
            'last_name': Scholtz,
            'email': ascholtz3@nature.com,
            'gender': Female,
            'ip_address': 241.193.98.45,
        }

         {
            'id': 5,
            'first_name': Tracy,
            'last_name': Coggin,
            'email': tcoggin4@mapy.cz,
            'gender': Male,
            'ip_address': 147.201.35.30,
        }

         {
            'id': 6,
            'first_name': Laney,
            'last_name': Deme,
            'email': ldeme5@umn.edu,
            'gender': Male,
            'ip_address': 112.88.98.164,
        }

         {
            'id': 7,
            'first_name': Ashlie,
            'last_name': Le Estut,
            'email': aleestut6@nationalgeographic.com,
            'gender': Female,
            'ip_address': 48.51.98.194,
        }

         {
            'id': 8,
            'first_name': Gerard,
            'last_name': Ludy,
            'email': gludy7@qq.com,
            'gender': Male,
            'ip_address': 127.119.96.228,
        }

         {
            'id': 9,
            'first_name': Gawain,
            'last_name': Fenne,
            'email': gfenne8@google.es,
            'gender': Male,
            'ip_address': 244.31.100.124,
        }

         {
            'id': 10,
            'first_name': Olenka,
            'last_name': Stroulger,
            'email': ostroulger9@mlb.com,
            'gender': Female,
            'ip_address': 107.139.233.217,
        }
            
            ]    

        @app.route('/idara/api/v1.0/visitors', methods=['GET'])
        def get_visitors():
        return jsonify({'visitors': visitors})

        if __name__ == '__main__':
            app.run(debug=True)