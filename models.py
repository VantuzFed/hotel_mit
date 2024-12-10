from typing import List

from sqlalchemy import Column, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Clients(Base):
    __tablename__ = 'clients'

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(20), nullable=False)
    last_name = mapped_column(String(20), nullable=False)
    phone_number = mapped_column(String(15), nullable=False)
    document_id = mapped_column(String(20), nullable=False)
    middle_name = mapped_column(String(20))
    e_mail = mapped_column(String(30))

    bill: Mapped[List['Bill']] = relationship('Bill', uselist=True, back_populates='client')


class Employees(Base):
    __tablename__ = 'employees'

    id = mapped_column(Integer, primary_key=True)
    login = mapped_column(String(20), nullable=False)
    first_name = mapped_column(String(20), nullable=False)
    last_name = mapped_column(String(20), nullable=False)
    password_ = mapped_column(String(20), nullable=False)

    job_history: Mapped[List['JobHistory']] = relationship('JobHistory', uselist=True, back_populates='emp')
    bill: Mapped[List['Bill']] = relationship('Bill', uselist=True, back_populates='emp')


class Rooms(Base):
    __tablename__ = 'rooms'

    id = mapped_column(Integer, primary_key=True)
    room_number = mapped_column(String(10), nullable=False)
    class_ = mapped_column('class', String(20), nullable=False)
    price_per_day = mapped_column(Integer, nullable=False)
    available = mapped_column(TINYINT(1), server_default=text("'1'"))

    booking: Mapped[List['Booking']] = relationship('Booking', uselist=True, back_populates='room')


class Booking(Base):
    __tablename__ = 'booking'
    __table_args__ = (
        ForeignKeyConstraint(['room_id'], ['rooms.id'], name='booking_ibfk_1'),
        Index('room_id', 'room_id', unique=True)
    )

    id = mapped_column(Integer, primary_key=True)
    room_id = mapped_column(Integer, nullable=False)
    book_start = mapped_column(TIMESTAMP, nullable=False)
    book_end = mapped_column(TIMESTAMP, nullable=False)
    book_status = mapped_column(String(20), server_default=text("'Начало'"))

    room: Mapped['Rooms'] = relationship('Rooms', back_populates='booking')
    bill: Mapped[List['Bill']] = relationship('Bill', uselist=True, back_populates='book')


class JobHistory(Base):
    __tablename__ = 'job_history'
    __table_args__ = (
        ForeignKeyConstraint(['emp_id'], ['employees.id'], name='job_history_ibfk_1'),
        Index('emp_id', 'emp_id', unique=True)
    )

    id = mapped_column(Integer, primary_key=True)
    emp_id = mapped_column(Integer, nullable=False)
    occupation = mapped_column(String(20), nullable=False)
    start_date = mapped_column(TIMESTAMP, nullable=False)
    end_date = mapped_column(TIMESTAMP)

    emp: Mapped['Employees'] = relationship('Employees', back_populates='job_history')


class Bill(Base):
    __tablename__ = 'bill'
    __table_args__ = (
        ForeignKeyConstraint(['book_id'], ['booking.id'], name='bill_ibfk_1'),
        ForeignKeyConstraint(['client_id'], ['clients.id'], name='bill_ibfk_3'),
        ForeignKeyConstraint(['emp_id'], ['employees.id'], name='bill_ibfk_2'),
        Index('book_id', 'book_id', unique=True),
        Index('client_id', 'client_id'),
        Index('emp_id', 'emp_id')
    )

    id = mapped_column(Integer, primary_key=True)
    book_id = mapped_column(Integer, nullable=False)
    emp_id = mapped_column(Integer, nullable=False)
    client_id = mapped_column(Integer, nullable=False)
    price_total = mapped_column(Integer)

    book: Mapped['Booking'] = relationship('Booking', back_populates='bill')
    client: Mapped['Clients'] = relationship('Clients', back_populates='bill')
    emp: Mapped['Employees'] = relationship('Employees', back_populates='bill')
