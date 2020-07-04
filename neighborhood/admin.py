from django.contrib import admin

# Register your models here.
from .models import Person, Block, House, Resident

admin.site.register(Person)
admin.site.register(Block)
admin.site.register(House)
admin.site.register(Resident)