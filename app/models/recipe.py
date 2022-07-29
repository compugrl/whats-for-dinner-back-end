from app import db

class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash= db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)
    image_tnail = db.Column(db.String)
    image_sm = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("User", back_populates="recipe")

    def to_dict(self):
        response = {
            "recipe_id": self.recipe_id,
            "hash": self.hash,
            "label": self.label,
            "image_tnail": self.image_tnail,
            "image_sm": self.image_sm
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            hash=data_dict["hash"],
            label=data_dict["label"],
            image_tnail=data_dict["image_tnail"],
            image_sm=data_dict["image_sm"]
            )
