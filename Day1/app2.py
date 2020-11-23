from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    code = '''
<h1>Hello World!</h1>
<title>Flask Hello World</title>
<p>
<label>Name:</label><input type="text" width = "50"></input>
<input type="submit"></input>
</p>

'''
    return code