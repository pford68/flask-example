__author__ = 'Philip Ford'

from todo import *
import os


class BaseProfile:
    """ Abstract base class for profiles"""
    active = False

    def close(self):
        pass


class ProductionBaseProfile(BaseProfile):
    def __init__(self, active):
        self.active = active


class DevelopmentBaseProfile(BaseProfile):
    """Creates db tables and seeds the database in initialization
    and drops all tables on destruction
    """

    def __init__(self, active):
        self.active = active
        db.drop_all()
        db.create_all()
        items = [
            Todo("Check the Audi", "The TPM warning is on again."),
            Todo("Get suitcase", "I want the large Tumi wheeled duffel for the trip to Europe.")
        ]
        for item in items:
            db.session.add(item)
        db.session.commit()

    def __del__(self):
        db.drop_all()


if os.environ.get('FLASK_MODE') == "PRODUCTION":
    profile = ProductionBaseProfile(True)
else:
    profile = DevelopmentBaseProfile(True)
