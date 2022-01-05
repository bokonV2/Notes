import datetime
from peewee import *

db = SqliteDatabase('Notes.db')

class BaseModel(Model):
    class Meta:
        database = db

class Notes(BaseModel):
    id = IntegerField(primary_key=True, unique=True)
    title = TextField()
    message = TextField()
    color = TextField()
    date = DateField(default=datetime.date.today())
    pin = IntegerField(default=0)


class Config(BaseModel):
    style = TextField()

if __name__ == '__main__':
    # Notes.create_table()
    Notes.create(
        title="title",
        message="message",
        color="color",
    )
