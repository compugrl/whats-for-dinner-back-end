from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash = db.Column(db.String, nullable=False)
    shareAs = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)    
    menu_date = db.Column(db.String)
    favorite = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship("User", back_populates="recipe", lazy=True)

    def to_dict(self):
        response = {
            "id": self.id,
            "hash": self.hash,
            "shareAs": self.shareAs,
            "label": self.label,
            "menu_date": self.menu_date,
            "favorite": self.favorite,
            "image_url": self.image_url,
            "user_id": self.user_id
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            hash=data_dict["hash"],
            shareAs=data_dict["shareAs"],
            label=data_dict["label"],
            image_url=data_dict["image_url"],
            menu_date="",
            user_id=data_dict["user_id"],
            favorite=False
            )
