from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from auth import authenticate_user
from cab_allocation import allocate_cab, search_nearby_cabs
from monitoring import log_event

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

@app.route('/')
def home():
    return "Hello, Smart Cab!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if authenticate_user(username, password):
        access_token = create_access_token(identity=username)
        log_event(f"User {username} logged in")
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/allocate_cab', methods=['POST'])
@jwt_required()
def allocate():
    employee_location = request.json.get('employee_location')
    allocated_cab = allocate_cab(employee_location)
    return jsonify(allocated_cab=allocated_cab)

@app.route('/search_nearby_cabs', methods=['GET'])
@jwt_required()
def search():
    employee_location = request.args.get('location')
    cabs = search_nearby_cabs(employee_location)
    return jsonify(cabs=cabs)

if __name__ == '__main__':
    app.run(debug=True)
