from django.contrib import admin
from portal import models

# * Registro de modelos con las funciones por defecto
admin.site.register(models.Portal)
admin.site.register(models.About)
admin.site.register(models.External_link)
admin.site.register(models.Review)
admin.site.register(models.Welcome_message)