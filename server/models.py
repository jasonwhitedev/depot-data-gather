from server.extensions import db

class Depots(db.Model):
    """ Depots """
    __tablename__ = 'depots'
    id = db.Column(db.Integer, primary_key=True)
    depot_name = db.Column(db.String(),)
    depot_number = db.Column(db.Integer())
    in_use = db.Column(db.Boolean())

    def serialize(self):
        """ serialize """
        return {
            "id": self.id,
            "depot_name": self.depot_name,
            "depot_number": self.depot_number,
            "in_use": self.in_use,
        }

def __init__(
        self,
        depot_name,
        depot_number,
        in_use
    ):
    self.depot_name = depot_name
    self.outcome_title = depot_number
    self.in_use = in_use