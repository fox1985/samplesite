from django.contrib import admin

# Register your models here.
from testapp.models import Spare, Machine, Note, PrivateMessage, Message

admin.site.register(Spare)

admin.site.register(Machine)

#admin.site.register(Note)

#admin.site.register(Message)

admin.site.register(PrivateMessage)