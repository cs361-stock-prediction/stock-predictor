from bokeh.plotting import figure, output_file, show

def fileToString(filename):
    html = open(filename)
    page = html.read()
    html.close()
    return page

def main():
    page = fileToString('/templates/prediction.html').format(**locals())
    browseLocal(page)