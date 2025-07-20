from mongoengine import Document, StringField, IntField

class Product(Document):
    barcode = StringField(required=True, unique=True)
    material= IntField()
    name = StringField()
    brand = StringField()
    description = StringField()
    image = StringField()
    category = StringField(default="Uncategorized")

    meta = {'collection': 'products'}
