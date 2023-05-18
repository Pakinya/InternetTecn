from django.contrib import admin

# Register your models here.
from .models import Artiles

admin.site.register(Artiles)

from .models import Goroskop

admin.site.register(Goroskop)