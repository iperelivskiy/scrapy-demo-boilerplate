import os
import datetime as dt

import peewee


DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'auto.db')
conn = peewee.SqliteDatabase(DB_PATH)


class BaseModel(peewee.Model):
    """
    Base model just to specify connection params.
    """
    class Meta:
        database = conn


class AutoPrice(BaseModel):
    """
    Auto price model where brand, model and price are stored.
    """
    brand = peewee.CharField()
    model = peewee.CharField()
    price = peewee.DecimalField()
    scraped_at = peewee.DateTimeField(default=dt.datetime.now)


if not AutoPrice.table_exists():
    """
    Create table if not exists.
    """
    result = AutoPrice.create_table()
