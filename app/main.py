from flask import Flask, request, render_template
from models.headers import RawHeaders
app = Flask(__name__)

_template_vars = {}

@app.route("/",  methods=["GET"])
def home():

    _raw = RawHeaders(request)
    _data = _raw.get_headers()

    _template_vars = {
        "page": {
            "title": "Home"
        },
        "result": _data
    }
    return render_template("pages/results.html", locals=_template_vars)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)