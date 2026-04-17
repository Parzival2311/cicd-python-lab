from flask import Flask

# CRITICAL: The variable MUST be named 'application'
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1>CI/CD Pipeline is Live!</h1><p>Version 2.0: Automated Update.</p>"

# DO NOT specify a port like 5000; Beanstalk handles this automatically
if __name__ == "__main__":
    application.run()
