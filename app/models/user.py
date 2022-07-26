from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    days_to_display = db.Column(db.Integer, nullable=False)
    menu_date = db.Column(db.Date)
    favorite = db.Column(db.Boolean)
    recipe = db.relationship('Recipe', back_populates="user", lazy=True)
    shopping_list = db.relationship('Shopping_list', back_populates="user", lazy=True)

    def to_dict(self):
        response = {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "days_to_display": self.days_to_display,
            "menu_date": self.menu_date,
            "favorite": self.favorite
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            name=data_dict["name"],
            email=data_dict["email"],
            days_to_display=data_dict["days_to_display"],
            menu_date=data_dict["menu_date"],
            favorite=data_dict["favorite"]
            )
