from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

# Homework - adding Hooks
@app.before_request
def log_request():
    print(f"[before_request] {request.method} {request.path}")

@app.after_request
def add_header(response):
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response # has to return the response object

@app.teardown_request
def log_exception(exception):
    if exception:
        print(f"[teardown_request] Exception: {exception}")

# 1 welcome
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to Flask API!</h1>"

# 2 about
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "name": "Sonya G",
        "course": "MCON-504 - Backend Development",
        "semester": "Spring 2025"
    })

# 3 Greeting
@app.route("/greet/<name>", methods=["GET"])
def greet():
    return "<p>Hello, {name}! Welcome to Flask.</p>"

# 4 calculate
# made some changes for exception handling

@app.route("/calculate", methods=["GET"])
def calculate():
    #get parameteres
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    operation = request.args.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1/ num2
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
    return jsonify(data)



# 6 status code
@app.route("/status/<int:code>", methods=["GET"])
def status(code):
    return f"This is a {code} status response", code

if __name__ == "__main__":
    app.run(debug=True, port=5000)