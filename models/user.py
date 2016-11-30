#!/usr/bin/python3

import models.modelBase
import models.address
import sqlalchemy
import sqlalchemy.orm


class User(models.modelBase.Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    fullname = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    addresses = sqlalchemy.orm.relationship("Address", order_by=models.address.Address.id, back_populates="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
