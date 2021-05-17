import flask

app = flask.Flask('main.py')


@app.route('/')
def index():
    return flask.render_template("index.html")


app.run()
