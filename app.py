from sqlalchemy.orm import sessionmaker
from main import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Insert 2 users
u1 = User(name="FromPython", age=20)
u2 = User(name="Ayza", age=19)

session.add_all([u1, u2])
session.commit()

print("Inserted:", u1.id, u1.name, u1.age)
print("Inserted:", u2.id, u2.name, u2.age)

# Read all users
users = session.query(User).all()
print("\nAll users:")
for u in users:
    print(u.id, u.name, u.age)

session.close()
