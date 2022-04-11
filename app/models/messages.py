from ..extensions import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    current_user = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<Messages %r>' % self.title
