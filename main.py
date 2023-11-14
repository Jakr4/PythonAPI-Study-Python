from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id":user_id,
        "name":"Jack Rinck",
        "email":"jack.rinck.iv@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/")
def home():
    return "Home"

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201
        

#GET    retreive some value from a resource
#POST   create a resource 
#PUT    update a resource
#DELETE delete a resource

if __name__ == "__main__":
    app.run(debug=True)