from flask import Flask
import os

app = Flask(__name__)

# https://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT
port = int(os.getenv("PORT"))


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
