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

# ----------------------
# $$$$$$$ MAIN $$$$$$$$
# ----------------------

def main():
    
    print("STARTING PROCESS")
        
    INPUT_VALUE = ""
    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))  # This doesn't work in jupyter
    SETTING_PATH = CURRENT_PATH + os.sep + "settings.json"
    json_readed = jr.read_json_to_dict(json_fullpath=SETTING_PATH)
    
    SERVER_RUNNING = json_readed["server_running"]
    
    print(SETTING_PATH)
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. Please, allow it to run it.")
            
if __name__ == "__main__":
    main()