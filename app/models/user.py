from app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)    
    recipe = db.relationship('Recipe', secondary="user_recipe")
    shopping_list = db.relationship('Shopping_list', back_populates="user", lazy=True)

    def to_dict(self):
        response = {
            "uid": self.uid,
            "name": self.name,
            "email": self.email,
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            name=data_dict["name"],
            email=data_dict["email"],
            )
