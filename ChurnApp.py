from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask import Flask
import os

app = Flask(__name__)
FlaskJSON(app)

@app.route('/status')
def status():
    return json_response(status = 'Online')

@app.route('/offers')
@app.route('/offers/<offer_type>')
def offers(offer_type = None):
    if str.lower(offer_type) == 'credit':
        churntype = 'CC_'
    elif str.lower(offer_type) == 'savings':
        churntype = 'SA_'
    elif str.lower(offer_type) == 'checking':
        churntype = 'CA_'
    else:
        raise ValueError('You have not selected a valid offer type.')
    return json_response(offer_type = offer_type, offers = [x for x in os.listdir('JSON') if x.startswith(churntype)])

@app.route('/offers/<offer_type>/<offer_name>')
def offer_names(offer_name = None):
    pass




if __name__ == '__main__':
    app.run()

