from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about1,name='about'),
    path('blog',views.blog,name='blog'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_signup',views.admin_signup,name='admin_signup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_index',views.admin_index,name='admin_index'),

    path('admin_reservation',views.admin_reservation,name='admin_reservation'),
    path('admin_newreservation_form_submission',views.admin_newreservation_form_submission,name='admin_newreservation_form_submission'),

    path('admin_editreservation/<int:id>',views.admin_editreservation,name='admin_editreservation'),
    path('admin_editreservation_update_form/<int:id>',views.admin_editreservation_update_form,name="admin_editreservation_update_form"),
    path('admin_editreservation_delete/<int:id>',views.admin_editreservation_delete,name="admin_editreservation_delete"),




    
    path('admin_equipment',views.admin_equipment,name='admin_equipment'),
    path("admin_equipment_form_submission",views.admin_equipment_form_submission,name="admin_equipment_form_submission"),

    path('admin_packages',views.admin_packages,name='admin_packages'),
    path('admin_categories',views.admin_categories,name='admin_categories'),


    path('admin_userlist',views.admin_userlist,name='admin_userlist'),
    path('admin_invoice1',views.admin_invoice1,name='admin_invoice1'),
    path('admin_invoiceconfig',views.admin_invoiceconfig,name='admin_invoiceconfig'),
    path('admin_editinvoice',views.admin_editinvoice,name="admin_editinvoice"),
    path('admin_invoice_form_submission',views.admin_invoice_form_submission,name='admin_invoice_form_submission'),


    path('admin_newreservation',views.admin_newreservation,name='admin_newreservation'),
    path('add_reservation_form_submission',views.add_reservation_form_submission,name="add_reservation_form_submission"),

    path('admin_addequipment',views.admin_addequipment,name='admin_addequipment'),
    path('admin_editequipment/<int:id>',views.admin_editequipment,name='admin_editequipment'),
    path('admin_photos',views.admin_photos,name='admin_photos'),
    path('admin_editequipment_update_form/<int:id>',views.admin_editequipment_update_form,name="admin_editequipment_update_form"),
    path('admin_editequipment_delete/<int:id>',views.admin_editequipment_delete,name="admin_editequipment_delete"),



    path('admin_adduser',views.admin_adduser,name='admin_adduser'),
    path('admin_adduser_form_submission',views.admin_adduser_form_submission,name="admin_adduser_form_submission"),
    path('admin_edituser/<int:id>',views.admin_edituser,name='admin_edituser'),
    path('admin_edituser_update_form/<int:id>',views.admin_edituser_update_form,name="admin_edituser_update_form"),
    path('admin_edituser_delete/<int:id>',views.admin_edituser_delete,name="admin_edituser_delete"),





    path('admin_addpackages',views.admin_addpackages,name='admin_addpackages'),
    path('admin_addpackage_form_submission',views.admin_addpackage_form_submission,name='admin_addpackage_form_submission'),
    path('admin_editpackages/<int:id>',views.admin_editpackages,name='admin_editpackages'),
    path('admin_editpackages_update_form/<int:id>',views.admin_editpackages_update_form,name="admin_editpackages_update_form"),
    path('admin_editpackages_delete/<int:id>',views.admin_editpackages_delete,name='admin_editpackages_delete'),



    path('admin_addcategories',views.admin_addcategories,name='admin_addcategories'),
    path('admin_addcategories_form_submission',views.admin_addcategories_form_submission,name="admin_addcategories_form_submission"),
    path('admin_editcategories/<int:id>',views.admin_editcategories,name='admin_editcategories'),
    path('admin_editcategories_update_form/<int:id>',views.admin_editcategories_update_form,name="admin_editcategories_update_form"),
    path('admin_editcategories_delete/<int:id>',views.admin_editcategories_delete,name="admin_editcategories_delete"),


    path('user_cart',views.user_cart,name='user_cart'),
    path('user_constructiontool',views.user_constructiontool,name='user_constructiontool'),
    path('user_drill',views.user_drill,name='user_drill'),
    path('user_drillcheck',views.user_drillcheck,name='user_drillcheck'),
    path('user_home',views.user_home,name='user_home'),
    path('user_index',views.user_index,name='user_index'),
    path('user_outdoorparty',views.user_outdoorparty,name='user_outdoorparty'),
    path('user_sport',views.user_sport,name='user_sport'),
    path('store_reg1_data',views.store_reg1_data,name='store_reg1_data'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('logout_page',views.logout_page,name='logout_page'),
    path('contact_reg_form_sub',views.contact_reg_form_sub,name='contact_reg_form_sub'),
    path('store_reg2_data',views.store_reg2_data,name='store_reg2_data'),
    path('login',views.login,name="login"),
    path('logout_user',views.logout_user,name='logout_user'),

    path('user_drill_form_submission',views.user_drill_form_submission,name="user_drill_form_submission"),
    path('check_user_drill_form_submission',views.check_user_drill_form_submission,name="check_user_drill_form_submission"),
    
    path('checkout',views.checkout,name="checkout"),
    path('user_cart_form_submission',views.user_cart_form_submission,name="user_cart_form_submission")
]


