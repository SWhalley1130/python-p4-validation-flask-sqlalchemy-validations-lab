from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, unique=True, nullable=False)
    phone_number=db.Column(db.Integer)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, string):
        names=db.session.query(Author.name).all()
        if not string:
            raise ValueError("Name field is required.")
        elif string in names:
            raise ValueError("Name must be unique.")
        return string

    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) !=10:
            raise ValueError('Phone number must be 10 digits long.')
        return number

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    content=db.Column(db.String)
    summary=db.Column(db.String)
    category=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    @validates('summary')
    def validate_summary(self, key, string):
        if len(string)>250:
            raise ValueError("Summary has a max of 250 characters.")
        return string

    @validates('content')
    def validate_content(self, key ,string):
        if len(string)<250:
            raise ValueError("Content must be at least 250 characters.")
        return string
    
    @validates('category')
    def validate_category(self, key, string):
        categories=['Fiction', 'Non-Fiction']
        if string not in categories:
            raise ValueError("Category must be Fiction or Non-Fiction.")
        return string 
    
    @validates('title')
    def validate_title(self, key,string):
        click_bait=['Won\'t Believe', 'Secet', 'Top', 'Guess']
        if string not in click_bait:
            raise ValueError("Title must be click-bait.")
        return string
