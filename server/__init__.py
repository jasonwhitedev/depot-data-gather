from flask import Flask, request
from flask_cors import CORS

from server.config import config
from server.extensions import db, migrate
from server.models import Depots


def create_app(config_name):
    app = Flask(__name__)

    # Enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # Config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Routes
    @app.route('/depots', methods=['GET', 'POST'])
    def all_depots():
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()
            depot = Depots()
            depot.depot_name = post_data.get('depot_name')
            depot.depot_number = post_data.get('depot_number')
            depot.in_use = post_data.get('in_use')

            db.session.add(depot)
            db.session.commit()      

            response_object['depots'] = 'Depot added!'
            return response_object

        else:
            depots = Depots.query.all()
            records = [z.serialize() for z in depots]
            return records
            
    # Return Flask app
    return app
