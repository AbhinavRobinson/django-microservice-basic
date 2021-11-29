from main import app, db
from flask_migrate import Migrate, migrate

migrate = Migrate(app, db)
