from flask import Flask

app=Flask(__name__)

@app.route("/<string:param>")
def index(param):
	return "This is what you entered" + param
