from flask import Flask 
app = Flask(__name__)
@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello, World!?"

app.config["DEBUG"]=True

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print value+1
	return "correct int"

@app.route("/float/<float:value>")
def float_type(value):
	print value+1
	return "correct float"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct path"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

if __name__ == "__main__":
	app.run()
