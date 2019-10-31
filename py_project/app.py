import yaml
import mysql.connector
import json
from flask import Flask, request, jsonify
from py_project.models.dog import Dog

app = Flask(__name__)

with open("py_project/db/config.yaml", 'r') as ymlfile:
    config = yaml.load(ymlfile)


@app.route('/name', methods=['GET'])
def get_name():
    dog = Dog()
    dog.name = 'salsicha'
    dog.nature = 'brave'
    dog.trick = 'play dead'

    response = json.dumps(dog.__dict__, indent=4)
    return response


@app.route('/give_name', methods=['POST'])
def naming_dog():
    content = request.get_json();
    print(content)
    dog = Dog()
    dog.name = content['name']
    dog.nature = content['nature']
    dog.trick = content['trick']
    insert_string = "INSERT INTO dogsDb(name, nature, trick) VALUES (%s, %s)", (dog.name, dog.nature, dog.trick)

    cursor = create_connection().cursor()
    cursor.execute(insert_string)

    create_connection().commit()
    cursor.close()
    return jsonify(message='Done',
                   statusCode=201)


def create_connection():
    connection = mysql.connector.connect(host=config['host'],
                                         database=config['database'],
                                         user=config['user'],
                                         password=config['password'],
                                         port=config['port'])
    return connection


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
