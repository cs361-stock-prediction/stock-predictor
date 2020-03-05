import os

from flask import Flask, render_template, send_from_directory

# for login: https://www.youtube.com/watch?v=8aTnmsDMldY

webserver = Flask(__name__)


# serve main files
@webserver.route("/")
def main():
    return render_template("index.html")


# serve favicons
@webserver.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(webserver.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@webserver.route('/favicon-16x16.png')
def favicon16():
    return send_from_directory(os.path.join(webserver.root_path, 'static'), 'favicon-16x16.png', mimetype='image/vnd.microsoft.icon')


@webserver.route('/favicon-32x32.png')
def favicon32():
    return send_from_directory(os.path.join(webserver.root_path, 'static'), 'favicon-32x32.png', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    webserver.run(debug=True, host="0.0.0.0", port=4096)
