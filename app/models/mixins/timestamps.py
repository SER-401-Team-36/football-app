from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, DateTime, func


class HasTimestamps(object):
    @declared_attr
    def time_created(cls):
        return Column(DateTime(timezone=True), server_default=func.now())

    @declared_attr
    def time_updated(cls):
        return Column(DateTime(timezone=True), onupdate=func.now())
