from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

# 1 welcome
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to Flask API!</h1>"

# 2 about
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "name": "Your Name",
        "course": "MCON-504 - Backend Development",
        "semester": "Spring 2025"
    })

# 3 Greeting
@app.route("/greet/Leah", methods=["GET"])
def greet():
    return "<p>Hello, Leah! Welcome to Flask.</p>"

# 4 calculate

@app.route("/calculate", methods=["GET"])
def calculate():
    #get parameteres
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    operation = request.args.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1/ num2;
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({
        "result": result,
        "operation": operation
    })


# 5 echo
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    data["echoed"] = True
    return jsonify({data})



# 6 status code
@app.route("/status/<int:code>", methods=["GET"])
def status(code):
    return f"This is a {code} status response", code

if __name__ == "__main__":
    app.run(debug=True)