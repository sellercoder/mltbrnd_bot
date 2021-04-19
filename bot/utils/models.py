# IMPORTS ##################################################
# orator packages ##########################################
from orator import Model
from orator.orm import belongs_to
from orator.orm import has_many
from orator.orm import has_many_through
from orator.orm import scope
from orator import accessor
# database connect #########################################
from utils.connector import db


class Page(Model):
    __guarded__ = ['created_at', 'updated_at']

class Provider(Model):
    __appends__ = ['plans']
    __visible__ = ['id', 'name', 'description', 'cover', 'plans']
    __guarded__ = ['created_at', 'updated_at']

    @has_many
    def plans(self):
        return Plan


class Plan(Model):
    __visible__ = ['id', 'name', 'description', 'price']
    __appends__ = ['provider']
    __guarded__ = ['created_at', 'updated_at']

    @belongs_to
    def provider(self):
        return Provider

