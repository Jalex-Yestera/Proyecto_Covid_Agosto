# contains the functionality that starts the Flask Api @Jalex-Yestera
'''There are two GET functions:
    i. One that must allow to receive an group_id and will return a json with
    one attribute called “token” with the S value (explained below). This
    function must only return the S value in a json if the group_id received
    is equal to N (explained below). Otherwise, it must return a string
    with a message of error.

    ii. Another that must allow you to receive a token_id value and, if
    token_id is equal to S , return the json that contains the information of
    the dataframe ( df ). Otherwise, return a string with a message of error.

    1. N is the letter of your group concatenated with the sum of the
    ages of the participants. Examples: “A103”, “C86”.

    2. S is the letter of your group concatenated with the
    multiplication of the DNIs of the participants of the group.
    Example: “B85918591859851”, “D635154795182”'''

import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
import pandas

# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")  # Default path
def default():
    # Redirect
    #return redirect("http://aiconscience.ddns.net", code=302)
    #return str(request.args)
    return Print('Api working')

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get', methods=['GET'])
def get():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['id']
    return request.args

# A route to return all of the available entries in our catalog.
@app.route('/api/test/', methods=['GET'])
def api_all():
    restaurant_id = None
    if 'id' in request.args:
        restaurant_id = int(request.args['id'])
    
    if restaurant_id == 1:
        return "{'json': true}"
    elif restaurant_id == 99:
        return jsonify(col_1=[3, 2, 1, 0], col_2=['a', 'b', 'c', 'd'])
    else:
        return "This is a message of error" + "<br>" + "<br>" + str(request.args)

# ----------------------
# $$$$$$$ MAIN $$$$$$$$
# ----------------------

def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "\\settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()