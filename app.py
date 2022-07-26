
from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
from test import all_together

import json
from bson import ObjectId
#from utils import import_to_database, objectid_to_string

# Create the Flask app
app = Flask(__name__)
# Enable CORS
CORS(app)

#===============================================================================
# database_results ()
#===============================================================================
@app.route('/DataBase', methods=['POST','GET'])
def database_results(requirement=None,pattern=None, technology=None, language=None):
    """
    API Call to database
    Arguments:
        requirement: Required (sent as URL query parameter from API Call)
        pattern: Optional (sent as URL query parameter from API Call)
        technology: Optional (sent as URL query parameter from API Call)
        language: Optional (sent as URL query parameter from API Call)
    Returns:
        A JSON containing the results collected from the database.
    """

    # Parse URL-encoded parameters
    requirement = request.args.get('requirement', type=str)  # Required: if key doesn't exist, returns None
    pattern = request.args.get('pattern', default=None,type=str) # Optional: if key doesn't exist, returns None
    technology = request.args.get('technology', default=None, type=str)  # Optional: if key doesn't exist, returns None
    language = request.args.get('language', default=None, type=str)  # Optional: if key doesn't exist, returns None

    if requirement is None:
        return unprocessable_entity()
    else:
        results=all_together(requirement,pattern,technology,language)
        results=JSONEncoder().encode(results)
        #print(results)
        # Compose and jsonify respond
        #message = {'status': 200,'message': 'The request was fulfilled.','results': results}
        #resp = message
        #resp.status_code = 200
    #import json
    #results = json.dumps(results.json(), indent=4)
    return results

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

#JSONEncoder().encode(analytics)
def objectid_to_string(dict_obj):
    """
    Convert all fields of dict that are ObjectIds to str.
    Arguments:
        dict_obj: A dict object.
    Returns:
        A dict object with Pymongo ObjectId as string.
    """

    for key in dict_obj:
        if isinstance(dict_obj[key], ObjectId):
            dict_obj[key] = str(dict_obj[key])

    return dict_obj
#===============================================================================
# errorhandler ()
#===============================================================================
@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + ' --> Please check your data payload.',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp
@app.errorhandler(422)
def unprocessable_entity(error=None):
    message = {
        'status': 400,
        'message': 'Unprocessable Entity: ' + request.url + ' --> Missing or invalid parameters.',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp
@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'status': 500,
        'message': 'The server encountered an internal error and was unable to complete your request. ' + error,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
