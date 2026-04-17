from flask import Flask
application = Flask(__name__) [cite: 146, 147]

@application.route('/') 
def hello_world(): [cite: 148]
    # This string is what you will update to test your automated deployment
    return "<h1>CI/CD Pipeline is Live!</h1><p>Version 1.0: Initial Deployment.</p>" [cite: 149]

if __name__ == "__main__": [cite: 150]
    application.run(debug=True) [cite: 151]
