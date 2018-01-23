from flask_cors import *
from flask import Flask, render_template, Response

app = Flask(__name__, static_folder='user_photo')
CORS(app, supports_credentials=True) # 这一句是关键


@app.route('/allpeople')
def getPeople():
    return json.dumps(os.listdir(userFolder))


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # ,  debug=True
