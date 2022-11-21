from django.contrib import admin
from .models import Country
from .models import Doctor
from .models import Disease
from .models import Diseasetype
from .models import Discover
from .models import Record
from .models import Users
from .models import Publicservant
from .models import Specialize


# Register your models here.
admin.site.register(Country)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Diseasetype)
admin.site.register(Discover)
admin.site.register(Record)
admin.site.register(Users)
admin.site.register(Publicservant)
admin.site.register(Specialize)
