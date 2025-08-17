class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
