#!/usr/bin/python3

import sqlalchemy
import sqlalchemy.orm
import models.user
import models.modelBase

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

models.modelBase.Base.metadata.create_all(engine)

ed_user = models.user.User(name='ed', fullname='Ed Jones', password='edspassword')
print(str(ed_user.id))

# NB: "Session" is a custom-made class, and "session" is an instance of that class
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

session.add(ed_user)

findEd = session.query(models.user.User).filter_by(name='ed').first()
print(findEd)

session.add_all([
    models.user.User(name='wendy', fullname='Wendy Williams', password='foobar'),
    models.user.User(name='mary', fullname='Mary Contrary', password='xxg527'),
    models.user.User(name='fred', fullname='Fred Flinstone', password='blah')])

ed_user.password = 'f8s7ccs'

print(session.dirty)
print(session.new)

session.commit()

print(ed_user.id)
