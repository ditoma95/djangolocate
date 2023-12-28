from django.contrib import admin
from locimo.models import *

# Register your models here.
class AdminProprio(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'sexe', 'birthdate', 'address')

class AdminAgenceimo(admin.ModelAdmin):
    list_display =('agency_name', 'background_image', 'profile_image', 'description', 'date_created')

class AdminContratelectronique(admin.ModelAdmin):
    list_display = ('nom_vendeur', 'nom_prenant')

class AdminConditionlocation(admin.ModelAdmin):
    list_display = ('type_location', 'type_construction', 'type_sanitaire', 'type_source_eau')



admin.site.register(Proprio, AdminProprio)
admin.site.register(Agenceimo, AdminAgenceimo)
admin.site.register(Contratelectronique, AdminContratelectronique)
admin.site.register(Conditionlocation, AdminConditionlocation)