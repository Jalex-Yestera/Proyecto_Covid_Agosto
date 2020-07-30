import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json

# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------
app = Flask(__name__)  # init
@app.route("/")  # Default path
def default():
    # Redirect
    return '''<h1> Api del grupo B</h1> <p> Añadir get_token?id= para conseguir el token</p>'''

@app.route("/give_me_id", methods =['GET'])
def give_id(): 
    x= request.args['id']
    return x
@app.route("/get_token", methods = ['GET'])
def get_token():
    clave = None
    yeison = { "token": "B23866390994081818446940" }
    if 'id' in request.args: 
        clave = str(request.args['id'])
    if clave == 'B145':
        return yeison
    else:
        return "Error al introducir la clave. Prueba con B145"
@app.route("/get_json", methods = ['GET'])
def get_json():
    token = None
    jason = d_averages.json
    if 'id' in request.args:
        token = str(request.args['id'])
    if token == 'B23866390994081818446940':
        return jason



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



    # S del grupo es B23866390994081818446940
    # N del grupo es B145