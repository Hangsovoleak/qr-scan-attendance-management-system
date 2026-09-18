from datetime import datetime, timezone

from sqlalchemy import (
Column, Integer, String, Date, Time, Float, Boolean, ForeignKey, DateTime, UniqueConstraint,
)
from sqlalchemy.orm import relationship
from Backend.database.base import Base

class AttendanceSession(Base):
    """
        One week's attendance window for a course, e.g.:
            Week:     4
            Date:     2026-09-18
            Start:    18:00
            End:      20:00
            Location: Classroom
            Radius:   100 meters

        Scope 5/6 ត្រូវការកូអរដោនេ GPS ពិតប្រាកដដើម្បីវាស់ចម្ងាយ។ ដូច្នេះ model មួយនេះត្រូវរក្សាទុកទិន្នន័យទាំងពីរ៖
        location_label៖ សម្រាប់បង្ហាញលើអេក្រង់
        latitude/longitude/radius_meters៖ សម្រាប់ប្រើក្នុងការផ្ទៀងផ្ទាត់ទីតាំងពិតប្រាកដនៅក្នុង Scope 5
        is_open គឺជាជំហាន "បើក/បិទ session" ចេញពី Build Order (Phase 3, step 17)។ ប្រសិនបើ session
        ត្រូវ បានបិទ (closed) ប្រព័ន្ធនឹងបដិសេធមិនទទួលការបោះត្រាវត្តមានថ្មីឡើយ ទោះបីជាថ្ងៃ និងម៉ោងនៅទាន់ពេលក៏ដោយ។
        លក្ខខណ្ឌនេះនឹងត្រូវពិនិត្យនៅក្នុង Scope 5។
    """
    __tablename__ = "attendance_session"
    __table_args__ = (
        UniqueConstraint("course_id", "week", name="uq_course_week"),
    )

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("course.id"), nullable=False)

    week = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    location_label = Column(String(150), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    radius_meters = Column(Integer, nullable=False)

    is_open = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    course = relationship("Course", back_populates="attendance_sessions")