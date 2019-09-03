# import dependencies
import os
from flask import Flask, render_template
from flask_cors import CORS

# bootstrap the app
app = Flask(__name__)
cors = CORS(app)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '5000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    return 'Congrats, you made your first website!!!'

@app.route('/search')
def search_tweet():
    return render_template('search.html')

@app.route('/submit-tweet')
def submit_tweet():
    return "tweet has been submitted"
    
# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)