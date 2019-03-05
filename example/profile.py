import os
from example import conn
from example.todo import Todo


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
        conn.drop_all()
        conn.create_all()
        items = [
            Todo(name="Check the Audi", description="The TPM warning is on again."),
            Todo(name="Get suitcase", description="I want the large Tumi wheeled duffel for the trip to Europe.")
        ]
        for item in items:
            conn.session.add(item)
        conn.session.commit()

    def __del__(self):
        # PF:  This is not being called when the application stops.
        conn.drop_all()


def init():
    if os.environ.get('FLASK_ACTIVE_PROFILE') == "PRODUCTION":
        profile = ProductionBaseProfile(True)
    else:
        profile = DevelopmentBaseProfile(True)
    return profile
