from app.database import SessionLocal
from app.models.admin import Admin
from app.core.security import hash_password


db = SessionLocal()


admin = Admin(
    username="mercy",
    hashed_password=hash_password("CyberDercy@2026")
)


db.add(admin)
db.commit()
db.close()


print("Admin created successfully")
