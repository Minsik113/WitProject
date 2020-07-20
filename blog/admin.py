from django.contrib import admin
from .models import Post #admin에서 관리하고자 하는 추가하고싶은 모델이있으면 추가하면됨.

# Register your models here.
admin.site.register(Post)
