from datetime import datetime, timezone

from sqlalchemy import Column, ForeignKey, UniqueConstraint, DateTime, Integer
from sqlalchemy.orm import relationship

from Backend.database.base import Base

class Enrollment(Base):
    """
    គូ (course_id, student_id) គឺមានលក្ខណៈពិសេស (Unique) — ពោលគឺ
    និស្សិតម្នាក់មិនអាចចុះឈ្មោះក្នុងវគ្គសិក្សាដដែលលើសពីពីរដងបានទេ។
    Table មួយនេះក៏ជាកន្លែងដែល Scope 6/7 (កំណត់ត្រាវត្តមាន និងស្ថិតិ) ត្រូវយកទៅប្រើ Join ជាមួយផងដែរ។
    """

    __tablename__ = "enrollment"
    __table_args__ = (UniqueConstraint("course_id", "student_id", name="uq_course_student"),)

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("course.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    enrollment_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    course = relationship("Course", back_populates="enrollments")
    student = relationship("Student", back_populates="enrollments")