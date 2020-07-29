# This module is dedicated to all Apis functions @ Jalex-Yestera
# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")
def default():
    # Redirect
    #return redirect("http://aiconscience.ddns.net", code=302)
    return str(Info(2,3,4))

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get', methods=['GET'])
def get():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/restaurants', methods=['GET'])
def api_restaurants():
    """
    127.0.0.1:5072/api/restaurants?id=0
    """
    restaurant_id = None
    if 'id' in request.args:
        restaurant_id = int(request.args['id'])
    
    restaurant, num_clients = random.randint(1, 9999), random.randint(0, 60)
    location = [random.randint(-100, 100), random.randint(-100, 100)]
    new_restaurant = Info(restaurant=restaurant, 
                            num_clients=num_clients, 
                            location=location)
        
    return str(new_restaurant)