from django.contrib.auth.models import User
from django.db.models import OneToOneField, ImageField, CASCADE, Model


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    avatar = ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return ""
