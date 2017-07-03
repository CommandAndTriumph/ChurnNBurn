from flask import Flask

app = Flask(__name__)

@ app.route('/status')
def status():
    return 'Server is online... Faggot'

app.run()
