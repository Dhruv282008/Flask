from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [{
    "ID": 1,
    "title": "Buy Groceries",
    "description": "Milk, Pizza",
    "done": False, 
}, {
    "ID": 2,
    "title": "Learn Python",
    "description": "Learn - Flask",
    "done": False
}]
@app.route("/")

def helloworld():
    return 'Hello World'

@app.route("/get-data")

def getdata():
    return jsonify({"data": tasks})
@app.route("/add-data", methods=["POST"])

def addTask():
    if(not request.json):
        return jsonify({
            "status": "error",
            "message": "Please provide the DATA"
        }, 400)

    task = {
        'ID': tasks[-1]['ID']+1,
        'title': request.json['title'],
        'description': request.json.get('description'),
        'done': False,
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task successfully created"
    })


if __name__ == "__main__": 
    app.run()

#API - Application Programming Interface.

#The GET Method - GET is used to request data from a specified resource. When you access a website’s page, your browser makes a get request to your API and your API is returning the front-end that is displayed in the browser.
# All the APIs that you create in Flask, by default, use GET Request. If you start your hello_world server and go to localhost:5000, you can see in your terminal that the browser made a GET request on the server/API.
# The POST Method - POST is used to send data to the server to create/update a resource.
# A user wants to sign up from the signup page. A user wants to change their password
# The PUT Method - PUT is used to send data to a server to create / update a resource.
# The basic difference between PUT and POST is that a POST request is when you can create multiple copies of the same resource. A PUT request, on the other hand means that you want to create only one copy of the resource, i.e. Signing Up a unique user.
# The DELETE Method - DELETE is used to delete a resource.

