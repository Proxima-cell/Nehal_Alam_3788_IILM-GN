from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import User, engine 
Session = sessionmaker(bind=engine)
session = Session ()
data = (session.query(User.age, func.count(User.id))
.filter(User.age>=18)
.order_by(User.age)
.filter(User.age<50)
.group_by(User.age)
.all()
)
for age, count in data:
    print(f"Age: {age}-{count} users")
