from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mult_table():
	if request.method == "GET":
		return render_template("form.html")
	elif request.method == "POST":
		return render_template("table.html", dim=request.form.get("size"))

@app.route("/test")
def test():
	return ("Made it to this route")