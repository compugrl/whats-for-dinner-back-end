from app import db

class Shopping_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    uid = db.Column(db.String, db.ForeignKey('user.uid'), nullable=False)
    user = db.relationship("User", back_populates="shopping_list")

    def to_dict(self):
        data_dict = {
            "id": self.id,
            "uid": self.uid,
            "ingredient": self.ingredient,
            "completed": self.completed
        }
        return data_dict
