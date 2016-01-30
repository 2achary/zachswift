from django.contrib import admin
from .models import Contact, Data, Deployment, Education, General, OS, Profile, Python, References, Testing, WorkHistory, Web, Blog

# Register your models here.
admin.site.register(Contact)
admin.site.register(Deployment)
admin.site.register(Education)
admin.site.register(General)
admin.site.register(OS)
admin.site.register(Profile)
admin.site.register(Python)
admin.site.register(References)
admin.site.register(Testing)
admin.site.register(Web)
admin.site.register(WorkHistory)
admin.site.register(Data)
admin.site.register(Blog)

