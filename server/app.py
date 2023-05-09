from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)
api = Api(app)

# Define a sample resource
class HelloWorld(Resource):
    def get(self):
        return jsonify({'message': 'Hello API'})

# Add the resource to the API
api.add_resource(HelloWorld, '/hello')

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://l2:5000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)

#https://askubuntu.com/questions/224392/how-to-allow-remote-connections-to-flask