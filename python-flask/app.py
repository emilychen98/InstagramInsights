from flask import Flask, render_template, url_for, request, redirect
from hashtagCounter import findHashtag

import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        req = request.get_json()
        counts = findHashtag(json.dumps(req))
        print(counts)
        return counts
    else:
        return "Hello World!"

# Incoming POST json
@app.route('/query-example', methods=['GET', 'POST'])
def query_example():
    print("got it")
    req = request.get_json()
    language = req.get('language') #if key doesn't exist, returns None
    something = req.get('something')
    print(language)
    print(something)
    return '''<h1>The language value is: {}</h1>'''.format(language)


if __name__ == "__main__":
    app.run(debug=True)
