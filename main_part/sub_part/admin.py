from django.contrib import admin

# Register your models here.
from . models import reg1,contact_reg,add_package_database,add_reservation_database,add_categories_database,add_user_database,add_equipment_database,add_newreservation_database,add_invoiceconfig_database,reg2,user_drill_database,check_user_drill_database,user_cart_database

admin.site.register(reg1)
admin.site.register(contact_reg)
admin.site.register(add_package_database)
admin.site.register(add_reservation_database)
admin.site.register(add_categories_database)
admin.site.register(add_user_database)
admin.site.register(add_equipment_database)
admin.site.register(add_newreservation_database)
admin.site.register(add_invoiceconfig_database)
admin.site.register(reg2)
admin.site.register(user_drill_database)
admin.site.register(check_user_drill_database)
admin.site.register(user_cart_database)