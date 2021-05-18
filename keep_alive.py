import flask
import threading

app = flask.Flask('main.py')


@app.route('/')
def index():
    return flask.render_template("index.html")


t = threading.Thread(target=app.run())
t.start()
