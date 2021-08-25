from django.http import request
from django.shortcuts import render,redirect
from . models import reg1,contact_reg,add_package_database,add_reservation_database,add_categories_database,add_user_database,add_equipment_database,add_newreservation_database,add_invoiceconfig_database,reg2,user_drill_database,check_user_drill_database,user_cart_database
from django.contrib import messages
from django.contrib.auth import logout

#multiple user login.
agraryans_user_name=''
# Create your views here.
def index(request):
    return render(request,'index.html')

def about1(request):
    return render(request,'about.html')    

def blog(request):
    return render(request,'blog.html')  

def portfolio(request):
    return render(request,'portfolio.html')      

def login(request):
    return render(request,'login.html')    

def contact(request):
    return render(request,'contact.html')

def admin_login(request):
    return render(request,'admin_login.html') 

def admin_signup(request):
    return render(request,'admin_signup.html')

def admin_home(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_home.html',{'agraryans_data':agraryans_data}) 

def admin_index(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_index.html',{'agraryans_data':agraryans_data})    

def admin_reservation(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_newreservation_database.objects.all()
    return render(request,'admin_reservation.html',{'agraryans_data':agraryans_data,"view_data":view_data}) 

def admin_newreservation_form_submission(request):
    if request.method=="POST":
        ex1=add_newreservation_database(unique_id=request.POST["unique_id"],
                                        dt_from=request.POST["dt_from"],
                                        dt_to=request.POST["dt_to"],
                                        payment=request.POST["payment"],
                                        price=request.POST["price"],
                                        security=request.POST["security"],
                                        tax=request.POST["tax"],
                                        deposit=request.POST["deposit"],
                                        total=request.POST["total"],
                                        borrow=request.POST["borrow"],
                                        back=request.POST["back"],
                                        items=request.POST["items"])   
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_reservation)                     
     
    return render(request,'admin_newreservation.html')


def admin_editreservation(request,id):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_newreservation_database.objects.get(id=id)
    return render(request,'admin_editreservation.html',{'agraryans_data':agraryans_data,'view_data':view_data})    

def admin_editreservation_update_form(request,id):
    if request.method=="POST":
        if add_newreservation_database.objects.filter(id=id).exists():
            ex1=add_newreservation_database.objects.filter(id=id).update(unique_id=request.POST["unique_id"],
                                                                         dt_from=request.POST["dt_from"],
                                                                         dt_to=request.POST["dt_to"],
                                                                         payment=request.POST["payment"],
                                                                         price=request.POST["price"],
                                                                        security=request.POST["security"],
                                                                        tax=request.POST["tax"],
                                                                        deposit=request.POST["deposit"],
                                                                       total=request.POST["total"],
                                                                        borrow=request.POST["borrow"],
                                                                         back=request.POST["back"],
                                                                       items=request.POST["items"]
                                                                   )
            messages.error(request,"your data has been updated successfully") 
            return redirect(admin_reservation)      
        else:
             return render(request,'admin_editreservation.html')



    
def admin_editreservation_delete(request,id):
    ex1=add_newreservation_database.objects.filter(id=id)
    ex1.delete()
    messages.error(request,"your data has been deleted successfully") 
    return redirect(admin_reservation)





def admin_equipment(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_equipment_database.objects.all()
    return render(request,'admin_equipment.html',{'agraryans_data':agraryans_data,"view_data":view_data})  

def admin_equipment_form_submission(request):
     if request.method=="POST":
        ex1=add_equipment_database(name=request.POST["name"],
                                   category=request.POST["category"],
                                   count=request.POST["count"],
                                   status=request.POST["status"],
                                   photos=request.POST.get("photos",False),
                                )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_equipment)                     
     
     return render(request,'admin_addequipment.html')     

def admin_packages(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_package_database.objects.all()
    return render(request,'admin_packages.html',{'agraryans_data':agraryans_data,'view_data':view_data})       

def admin_categories(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_categories_database.objects.all()
    return render(request,'admin_categories.html',{'agraryans_data':agraryans_data,"view_data":view_data})   

def admin_userlist(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_user_database.objects.all()
    return render(request,'admin_userlist.html',{'agraryans_data':agraryans_data,"view_data":view_data}) 

def admin_invoice1(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_invoiceconfig_database.objects.all()
    return render(request,'admin_invoice1.html',{'agraryans_data':agraryans_data,"view_data":view_data}) 

def admin_invoiceconfig(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_invoiceconfig.html',{'agraryans_data':agraryans_data})

def admin_invoice_form_submission(request):
     if request.method=="POST":
        ex1=add_invoiceconfig_database(order_no=request.POST["order_no"],
                                       issue_date=request.POST["issue_date"],
                                       due_date=request.POST["due_date"],
                                       created=request.POST["created"],
                                       status=request.POST["status"],
                                       total=request.POST["total"],
                                )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_invoice1)                     
     
     return render(request,'admin_invoiceconfig.html')


def admin_newreservation(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_newreservation.html',{'agraryans_data':agraryans_data})         

def add_reservation_form_submission(request):
    if request.method=="POST":
        ex1=add_reservation_database(unique_id=request.POST["unique_id"],
                                     dt_from=request.POST["dt_from"],
                                     dt_to=request.POST["dt_to"],
                                     payment=request.POST["payment"],
                                     price=request.POST["price"],
                                     security=request.POST["security"],
                                     deposit=request.POST["deposit"],
                                     tax=request.POST["tax"],
                                     total=request.POST["total"],
                                     borrow=request.POST["borrow"],
                                     back=request.POST["back"], 
                                   )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_reservation)              

    return render(request,'admin_newreservation.html')

def admin_addequipment(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_addequipment.html',{'agraryans_data':agraryans_data})  

def admin_editequipment(request,id):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_equipment_database.objects.get(id=id)
    return render(request,'admin_editequipment.html',{'agraryans_data':agraryans_data,'view_data':view_data}) 

def admin_editequipment_update_form(request,id):
    if request.method=="POST":
        if add_equipment_database.objects.filter(id=id).exists():
            ex1=add_equipment_database.objects.filter(id=id).update(name=request.POST["name"],
                                                                   category=request.POST["category"],
                                                                   count=request.POST["count"],
                                                                   status=request.POST["status"],
                                                                   photos=request.POST.get("photos",False),
                                                                   )
            messages.error(request,"your data has been updated successfully") 
            return redirect(admin_equipment)      
        else:
             return render(request,'admin_editequipment.html')



    
def admin_editequipment_delete(request,id):
    ex1=add_equipment_database.objects.filter(id=id)
    ex1.delete()
    messages.error(request,"your data has been deleted successfully") 
    return redirect(admin_equipment)








def admin_photos(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_photos.html',{'agraryans_data':agraryans_data}) 

def admin_addpackages(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    
    return render(request,'admin_addpackages.html',{'agraryans_data':agraryans_data}) 


def  admin_addpackage_form_submission(request):
    if request.method=="POST":
        ex1=add_package_database(name=request.POST["name"],
                                description=request.POST["description"],
                                items=request.POST["items"],
                                add_package_file=request.POST.get("add_package_file",False),
                                )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_packages)                     
     
    return render(request,'admin_addpackages.html')
def admin_editpackages(request,id):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_package_database.objects.get(id=id)
    return render(request,'admin_editpackages.html',{'agraryans_data':agraryans_data,'view_data':view_data})   

def admin_editpackages_update_form(request,id):
    if request.method=="POST":
        if add_package_database.objects.filter(id=id).exists():
            ex1=add_package_database.objects.filter(id=id).update(name=request.POST["name"],
                                                                  description=request.POST["description"],
                                                                   items=request.POST["items"],
                                                                   )
            messages.error(request,"your data has been updated successfully") 
            return redirect(admin_packages)      
        else:
             return render(request,'admin_editpackages.html')



    
def admin_editpackages_delete(request,id):
    ex1=add_package_database.objects.filter(id=id)
    ex1.delete()
    messages.error(request,"your data has been deleted successfully") 
    return redirect(admin_packages)

     


def admin_addcategories(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_addcategories.html',{'agraryans_data':agraryans_data}) 

def  admin_addcategories_form_submission(request):
    if request.method=="POST":
        ex1=add_categories_database(title=request.POST["title"],
                                    product=request.POST["product"],
                                    status=request.POST["status"]
                                   
                                )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_categories)                     
     
    return render(request,'admin_addcategories.html')    

def admin_editcategories(request,id):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_categories_database.objects.get(id=id)
    return render(request,'admin_editcategories.html',{'agraryans_data':agraryans_data,"view_data":view_data})  

def admin_editcategories_update_form(request,id):
    if request.method=="POST":
        if add_categories_database.objects.filter(id=id).exists():
            ex1=add_categories_database.objects.filter(id=id).update(title=request.POST["title"],
                                                                  product=request.POST["product"],
                                                                   status=request.POST["status"],
                                                                   )
            messages.error(request,"your data has been updated successfully") 
            return redirect(admin_categories)      
        else:
             return render(request,'admin_editcategories.html')

def admin_editcategories_delete(request,id):
    ex1=add_categories_database.objects.filter(id=id)
    ex1.delete()
    messages.error(request,"your data has been deleted successfully") 
    return redirect(admin_categories)             




def admin_editinvoice(request):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    return render(request,'admin_editinvoice.html',{'agraryans_data':agraryans_data})           

def admin_adduser(request):
    return render(request,'admin_adduser.html') 

def admin_adduser_form_submission(request):
    if request.method=="POST":
        ex1=add_user_database(name=request.POST["name"],
                               email_id=request.POST["email_id"],
                                password=request.POST["password"],
                                reg_date=request.POST["reg_date"],
                                role=request.POST["role"],
                                status=request.POST["status"],
                                )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(admin_userlist)                     
     
    return render(request,'admin_adduser.html')


def admin_edituser(request,id):
    agraryans_data=reg1.objects.get(user_name=agraryans_user_name)
    view_data=add_user_database.objects.get(id=id)
    return render(request,'admin_edituser.html',{'agraryans_data':agraryans_data,'view_data':view_data})

def admin_edituser_update_form(request,id):
    if request.method=="POST":
        if add_user_database.objects.filter(id=id).exists():
            ex1=add_user_database.objects.filter(id=id).update(name=request.POST["name"],
                                                              email_id=request.POST["email_id"],
                                                              password=request.POST["password"],
                                                              reg_date=request.POST["reg_date"],
                                                               role=request.POST["role"],
                                                              status=request.POST["status"],
                                                                   )
            messages.error(request,"your data has been updated successfully") 
            return redirect(admin_userlist)      
        else:
             return render(request,'admin_edituser.html')

def admin_edituser_delete(request,id):
    ex1=add_user_database.objects.filter(id=id)
    ex1.delete()
    messages.error(request,"your data has been deleted successfully") 
    return redirect(admin_userlist)               

def user_cart(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_cart.html',{'agraryans_data':agraryans_data}) 
   

def user_constructiontool(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_constructiontool.html',{'agraryans_data':agraryans_data}) 
   
def user_drill(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_drill.html',{'agraryans_data':agraryans_data}) 
      

def user_drillcheck(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_drillcheck.html',{'agraryans_data':agraryans_data})  
    
       

def user_home(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    
    return render(request,'user_home.html',{'agraryans_data':agraryans_data})  
    

def user_index(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_index.html',{'agraryans_data':agraryans_data})   
       

def user_outdoorparty(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_outdoorparty.html',{'agraryans_data':agraryans_data})   

     

def user_sport(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'user_sport.html',{'agraryans_data':agraryans_data})   

                      


def store_reg1_data(request):
    if  request.method=='POST':
        if reg1.objects.filter(user_name=request.POST['user_name']).exists():
            messages.error(request,'This username has already taken',extra_tags='login')
        elif reg1.objects.filter(email_id=request.POST['email_id']).exists():
            messages.error(request,'This Email id has already taken',extra_tags='login')

        else:
            ex1=reg1(user_name=request.POST['user_name'],
                 password=request.POST['password'],
                 c_password=request.POST['c_password'],
                email_id=request.POST['email_id'],
            )
            ex1.save()
            messages.error(request,'your data have been saved successfully',extra_tags='reg')
            return render(request,'admin_login.html')
    return render(request,'admin_signup.html')

def admin_login(request):
    if request.method=='POST':
        if reg1.objects.filter(user_name=request.POST['user_name'], password=request.POST['password']).exists():
            ex1=reg1.objects.get(user_name=request.POST['user_name'], password=request.POST['password'])
            global agraryans_user_name
            agraryans_user_name=ex1.user_name
            print("check:",agraryans_user_name)
            agraryans_data=reg1.objects.get(user_name=agraryans_user_name)

            return render(request,'admin_home.html',{'agraryans_data':agraryans_data})
        else:
            messages.error(request,'your username or password is incorrect',extra_tags='login')
            return render(request,'admin_login.html')

    return render(request,'admin_login.html')

def logout_page(request):
    logout(request)
    return render(request,'index.html')

def contact_reg_form_sub(request):
    if request.method=='POST':
        ex1=contact_reg(name=request.POST['name'],
                        email_id=request.POST['email_id'],
                        subject=request.POST['subject'],
                        message=request.POST['message'] ,
                        )
        ex1.save()
        messages.error(request,'your contact details has been saved successfully',extra_tags='contact')          
        return render(request,'index.html')      

   
def store_reg2_data(request):
    if  request.method=='POST':
        if reg2.objects.filter(user_name=request.POST['user_name']).exists():
            messages.error(request,'This username has already taken',extra_tags='login')
        elif reg2.objects.filter(email_id=request.POST['email_id']).exists():
            messages.error(request,'This Email id has already taken',extra_tags='login')

        else:
            ex1=reg2(user_name=request.POST['user_name'],
                     password=request.POST['password'],
                     c_password=request.POST['c_password'],
                     email_id=request.POST['email_id'],
            )
            ex1.save()
            messages.error(request,'your data have been saved successfully',extra_tags='reg')
            return render(request,'login.html')
    return render(request,'login.html')



def login(request):
    if request.method=='POST':
        if reg2.objects.filter(user_name=request.POST['user_name'], password=request.POST['password']).exists():
            ex1=reg2.objects.get(user_name=request.POST['user_name'], password=request.POST['password'])
            global agraryans_user_name
            agraryans_user_name=ex1.user_name
            print("check:",agraryans_user_name)
            agraryans_data=reg2.objects.get(user_name=agraryans_user_name)

            return render(request,'user_home.html',{'agraryans_data':agraryans_data})
        else:
            messages.error(request,'your username or password is incorrect',extra_tags='login')
            return render(request,'login.html')

    return render(request,'login.html')    


def logout_user(request):
    logout(request)
    return render(request,'index.html')





def user_drill_form_submission(request):
    if request.method=="POST":
        ex1=user_drill_database(quantity=request.POST["quantity"],
                               start_dt =request.POST["start_dt"],
                                end_dt=request.POST["end_dt"],
                               
                                )
        ex1.save()
      
        return redirect(user_drillcheck)                     
     
    return render(request,'user_drill.html')


def check_user_drill_form_submission(request):
    if request.method=="POST":
        ex1=check_user_drill_database(quantity=request.POST["quantity"],
                                      start_dt=request.POST["start_dt"],
                                      end_dt=request.POST["end_dt"],
                                      total=request.POST["total"],
                               
                                )
        ex1.save()
       
        return redirect(user_cart)                     
     
    return render(request,'user_drillcheck.html')    



def checkout(request):
    agraryans_data=reg2.objects.get(user_name=agraryans_user_name)
    return render(request,'checkout.html',{'agraryans_data':agraryans_data})  
 
  

def user_cart_form_submission(request):
    if request.method=="POST":
        ex1=user_cart_database(quantity=request.POST["quantity"],
                               price=request.POST["price"],
                               borrow=request.POST["borrow"],
                                back=request.POST["back"],
                               
                                )
        ex1.save()
        messages.error(request,"your data has been saved successfully")   
        return redirect(user_cart)                     
     
    return render(request,'user_cart.html')    
 