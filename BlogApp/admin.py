from django.contrib import admin

# Register your models here.
from BlogApp.models import Writeblog, Contact

admin.site.register(Writeblog)
admin.site.register(Contact)
