from flask import Flask, render_template

# for login: https://www.youtube.com/watch?v=8aTnmsDMldY

webserver = Flask(__name__)

@webserver.route("/")
def main():
	return render_template("base.html")

if __name__ == "__main__":
	webserver.run(debug=True, port=4096)