from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #unique=Trueで同じメールアドレス、空欄を許さなくなる。
    email = models.EmailField('メールアドレス', unique=True)