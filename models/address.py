#!/usr/bin/python3

import models.modelBase
import sqlalchemy
import sqlalchemy.orm


class Address(models.modelBase.Base):
    # Here we define our class variables. These are shared among all instances of this class.
    # They can be accessed as (for example) Address.id from inside the class or outside the class.
    __tablename__ = 'addresses'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email_address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))

    user = sqlalchemy.orm.relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
