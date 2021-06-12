from django.contrib import admin
from .models import shopDetail,productShop,productCategoy,locations
# Register your models here.

admin.site.register(shopDetail)
admin.site.register(locations)
admin.site.register(productShop)
admin.site.register(productCategoy)
