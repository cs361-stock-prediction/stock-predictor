from flask import Flask, render_template

# for login: https://www.youtube.com/watch?v=8aTnmsDMldY

webserver = Flask(__name__)

@webserver.route("/")
def main():
	return render_template("index.html")

if __name__ == "__main__":
	webserver.run(debug=True, host="0.0.0.0", port=4096)
