from datetime import datetime, timezone

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from Backend.database.base import Base

class Course(Base):
    """
    A course taught by one teacher, e.g.:
        name = "Python Backend Development"
        semester = 1
        academic_year = 2026
    """

    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    semester = Column(Integer, nullable=False)
    academic_year = Column(Integer, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))

    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")
    attendance_sessions = realtionship("AttendanceSession", back_populates="course", cascade="all, delete-orphan")