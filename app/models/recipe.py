from app import db

class Recipe(db.Model):
    rhash = db.Column(db.String, primary_key=True)
    shareAs = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)    
    user = db.relationship("User", secondary="user_recipe")

    def to_dict(self):
        response = {
            "rhash": self.rhash,
            "shareAs": self.shareAs,
            "label": self.label,
            "image_url": self.image_url,
            }
        return response

    @classmethod
    def create(cls, data_dict):
        return cls(
            rhash=data_dict["rhash"],
            shareAs=data_dict["shareAs"],
            label=data_dict["label"],
            image_url=data_dict["image_url"],
            )
