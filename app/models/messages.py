from ..extensions import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=False)
    category = db.relationship('Users',
                               backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<Messages %r>' % self.title
