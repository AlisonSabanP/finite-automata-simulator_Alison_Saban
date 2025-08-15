from flask import Flask
from api.routes import api  
app = Flask(__name__)

app.register_blueprint(api) 

@app.route('/')
def home():
    return 'hello from flask'

if __name__ == '__main__':
    app.run( port=1804) 
