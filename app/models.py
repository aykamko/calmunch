from sqlalchemy import Column, SmallInteger, Integer, String,\
        LargeBinary, DateTime, ForeignKey, Unicode
from sqlalchemy.orm import relationship
from app.database import Base

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key = True)
    name = Column(Unicode(64))
    blurb = Column(Unicode(140))
    location = Column(Unicode(140))
    sponsor = Column(Unicode(140))
    description = Column(Unicode(5000))
    food = Column(Unicode(280))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    contact = Column(Unicode(140))

    def __repr__(self):
        return '<Event %r>' % (self.name)
