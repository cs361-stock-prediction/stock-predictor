from bokeh.plotting import figure, output_file, show
import requests

app = Flask(__name__)

def fileToString(filename):
    html = open(filename)
    page = html.read()
    html.close()
    return page

def main():
    page = fileToString('/templates/prediction.html').format(**locals())
    browseLocal(page)
    resp = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=")
    json = resp.json()

    