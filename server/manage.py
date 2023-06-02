import os

from flask_migrate import Migrate

from server import create_app
from server.models import Depots

app = create_app(os.getenv('FLASK_ENV') or 'default')