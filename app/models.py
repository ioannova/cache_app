# -*- encoding: utf-8 -*-

from sqlalchemy import BINARY, Integer, ForeignKey, String, Boolean, Date, Time, Float, DateTime, Column, Table
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from app import db

class Cache(db.Model):
    __tablename__ = 'cache'

    id = Column(Integer, primary_key=True)
    key = Column(String(64), unique=True)
    value = Column(String(512))
    date = Column(DateTime, nullable=True)

    def __repr__(self):
        return '%s: %s' % (self.key, self.value)
    

    @hybrid_property
    def expiration(self):
        if self.date:
            return True if datetime.now() > self.date else False
        else:
            return False

    @hybrid_property
    def no_expiration(self):
        if self.date is None:
            return True
        return False