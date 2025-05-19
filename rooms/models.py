from django.db.models import CharField, DateTimeField, Model, TextField


class Room(Model):
    name: CharField = CharField(max_length=100, unique=True)
    description: TextField = TextField(blank=True)
    created_at: DateTimeField = DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
