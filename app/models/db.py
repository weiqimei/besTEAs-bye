from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BobaShop(db.Model):
    __tablename__ = 'boba_shops'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    image = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    hours = db.Column(db.String(25), nullable=False)

    # RELATIONSHIPS GO HERE
    # many to one relationship --> boba shops belongs to user
    user = db.relationship("User", back_populates="boba_shop")
    # one to many relationship --> boba shop has many reviews
    review = db.relationship("Review", back_populates="boba_shop", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "image": self.image,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "phone": self.phone,
            "hours": self.hours
        }


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    boba_shop_id = db.Column(db.Integer, db.ForeignKey("boba_shops.id"), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.Text, nullable=False)
    date = db.Column(db.TIMESTAMP(timezone=False), nullable=False)

    # RELATIONSHIPS GO HERE 
    # many to one relationship --> reviews belongs to user
    user = db.relationship("User", back_populates="review")  
    # many to one relationship --> reviews belongs to boba
    boba_shop = db.relationship("BobaShop", back_populates="review")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "boba_shop_id": self.boba_shop_id,
            "content": self.content,
            "picture": self.picture,
            "date": self.date
        }


# add likes table if needed later
