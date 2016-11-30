#!/usr/bin/python3

import sqlalchemy
import sqlalchemy.orm
import models.user
import models.modelBase
import models.address

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

models.modelBase.Base.metadata.create_all(engine)

ed_user = models.user.User(name='ed', fullname='Ed Jones', password='edspassword')
print(str(ed_user.id))

# "Session" is a custom-made class, and "session" is an instance of that class
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

# session.dirty shows modified records, session.new shows new records
print(session.dirty)
print(session.new)

# whatever we've changed/added in this session, commit the changes.
session.commit()

print(ed_user.id)

jack_user = models.user.User(name='jack', fullname='Jack Bean', password='gjffdd')
print(jack_user)
print(jack_user.addresses)

jack_user.addresses = [models.address.Address(email_address='jack@google.com'),
                       models.address.Address(email_address='j25@yahoo.com')]

print(jack_user.addresses[1])
print(jack_user.addresses[1].user)

session.add(jack_user)

print(session.dirty)
print(session.new)

session.commit()

q = session.query(models.user.User).join(models.address.Address).\
    filter(models.address.Address.email_address=='jack@google.com').all()

print(q)

print("Done!")