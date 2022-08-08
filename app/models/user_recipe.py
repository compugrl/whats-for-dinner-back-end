from app import db
from sqlalchemy.orm import backref

class UserRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String, db.ForeignKey('user.uid'))
    rhash = db.Column(db.String, db.ForeignKey('recipe.rhash'))
    menu_date = db.Column(db.String)
    favorite = db.Column(db.Boolean)
    user = db.relationship("User", backref=backref("user_recipe", cascade="all, delete-orphan"))
    recipe = db.relationship("Recipe", backref=backref("user_recipe", cascade="all, delete-orphan"))

    def to_dict(self):
        response = {
            "id": self.id,
            "uid": self.uid,
            "rhash": self.rhash,
            "menu_date": self.menu_date,
            "favorite": self.favorite
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            uid=data_dict["uid"],
            rhash=data_dict["rhash"],
            )
