from peewee import *

db = SqliteDatabase(database='db.db')


class Pen(Model):
    id = PrimaryKeyField(unique=True)
    brand = CharField()
    color = CharField()

    class Meta():
        database = db
        orfer_by = 'id'
