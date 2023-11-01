from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from app import app, db


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name="mobile")
        c2 = Category(name="tablet")
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        p1 = Product(name="iPhone 14", price=180000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=1)
        p2 = Product(name="iPhone 15", price=180000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=1)
        p3 = Product(name="ipad 10 ", price=180000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=2)
        p4 = Product(name="iPhone 14", price=180000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=1)
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        # db.create_all()
