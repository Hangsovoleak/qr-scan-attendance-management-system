from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from Backend.database.base import Base

class Student(Base):
    """
    ទិន្នន័យក្នុងជួរ (row) របស់ Student គឺប្រើជាលក្ខណៈ Global (មិនចំណុះឱ្យវគ្គសិក្សាណាមួយឡើយ) —
    និស្សិតម្នាក់អាចចុះឈ្មោះរៀនបានច្រើនវគ្គសិក្សា តាមរយៈ Join table ដែលមានឈ្មោះថា Enrollment។
    ចំណែកឯជួរឈរ "No." ដែលបង្ហាញនៅក្នុងតារាងរបស់គ្រូ គឺគ្រាន់តែជាលំដាប់ជួរនៅលើអេក្រង់ប៉ុណ្ណោះ
    មិនមែនជាទិន្នន័យ (field) ដែលរក្សាទុកក្នុង Database ទេ។
    """

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_no = Column(String(50), nullable=False, unique=True, index=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")