from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(AdminAcc)
admin.site.register(IndivAcc)
admin.site.register(TeamAcc)
admin.site.register(OrgAcc)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Notice)
admin.site.register(Pr)