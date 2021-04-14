from orator import Model
from orator import Schema
from orator import DatabaseManager
from data.config import DATABASES

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
