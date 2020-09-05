from django.contrib import admin
from .models import Person, Resident, House, Block, Employee, RoleEmployee, Role
# Register your models here.

admin.site.register(Person)
admin.site.register(Resident)
admin.site.register(House)
admin.site.register(Block)
admin.site.register(Employee)
admin.site.register(RoleEmployee)
admin.site.register(Role)
