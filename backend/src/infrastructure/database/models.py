from datetime import date, datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Text, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BirthdayModel(Base):
    __tablename__ = "birthdays"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False, index=True)
    company = Column(String(255), nullable=False, index=True)
    position = Column(String(255), nullable=False, index=True)
    birth_date = Column(Date, nullable=False, index=True)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        Index("idx_birthday_search", "full_name", "company", "position"),
    )


class ResponsiblePersonModel(Base):
    __tablename__ = "responsible_persons"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False, index=True)
    company = Column(String(255), nullable=False, index=True)
    position = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    assignments = relationship("DateResponsibleAssignmentModel", back_populates="responsible_person")

    __table_args__ = (
        Index("idx_responsible_search", "full_name", "company", "position"),
    )


class DateResponsibleAssignmentModel(Base):
    __tablename__ = "date_responsible_assignments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)
    responsible_person_id = Column(Integer, ForeignKey("responsible_persons.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    responsible_person = relationship("ResponsiblePersonModel", back_populates="assignments")

    __table_args__ = (
        Index("idx_date_responsible_unique", "date", "responsible_person_id", unique=True),
    )


class ProfessionalHolidayModel(Base):
    __tablename__ = "professional_holidays"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    date = Column(Date, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class PanelAccessModel(Base):
    __tablename__ = "panel_access"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    accessed_at = Column(DateTime, default=datetime.utcnow, nullable=False)

