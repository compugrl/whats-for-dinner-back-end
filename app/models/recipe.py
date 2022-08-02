from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash = db.Column(db.String, nullable=False)
    shareAs = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("User", back_populates="recipe")

    def to_dict(self):
        response = {
            "id": self.id,
            "hash": self.hash,
            "shareAs": self.shareAs,
            "label": self.label,
            "image_url": self.image_url
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            hash=data_dict["hash"],
            shareAs=data_dict["shareAs"],
            label=data_dict["label"],
            image_url=data_dict["image_url"]
            )
