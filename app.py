import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('./static/port.json') as f:
        data = json.load(f)
    return render_template('index.html', projects=data['projects'], info=data['info'])
    

if __name__ == '__main__':
    app.run(debug=False)
