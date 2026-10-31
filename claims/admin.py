from django.contrib import admin

# Register your models here.
from claims.models import Claim

admin.site.register(Claim)