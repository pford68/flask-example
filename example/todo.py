from example import conn


class Todo(conn.Model):
    __tablename__ = 'todo'
    id = conn.Column("id", conn.Integer, primary_key=True)
    name = conn.Column("name", conn.String(50), unique=True)
    description = conn.Column("description", conn.String(255), unique=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Todo(id='%d', name='%s', description='%s')>" % (self.id, self.name, self.description)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
