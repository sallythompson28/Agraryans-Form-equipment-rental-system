from django.db import models

# Create your models here.
class reg1(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    c_password=models.CharField(max_length=100)
    email_id=models.EmailField()

    

    def __str__(self):
      return self.user_name


class contact_reg(models.Model):
  name=models.CharField(max_length=100)
  email_id=models.EmailField()
  subject=models.CharField(max_length=100)
  message=models.TextField()




class add_package_database(models.Model):
  name=models.CharField(max_length=100)
  description=models.TextField()
  items=models.CharField(max_length=100)
  add_package_file=models.FileField(upload_to="documents",null=True)


class add_reservation_database(models.Model):
  unique_id=models.CharField(max_length=100)
  dt_from=models.CharField(max_length=100)
  dt_to=models.CharField(max_length=100)
  payment=models.CharField(max_length=100)
  price=models.CharField(max_length=100)
  security=models.CharField(max_length=100)
  deposit=models.CharField(max_length=100)
  tax=models.CharField(max_length=100)
  total=models.CharField(max_length=100)
  borrow=models.CharField(max_length=100)
  back=models.CharField(max_length=100)


class add_categories_database(models.Model):  
  title=models.CharField(max_length=100)
  product=models.CharField(max_length=100)
  status=models.CharField(max_length=100)

class add_user_database(models.Model):
  name=models.CharField(max_length=100)
  email_id=models.EmailField()
  password=models.CharField(max_length=100)
  role=models.CharField(max_length=100)
  status=models.CharField(max_length=100)
  reg_date=models.CharField(max_length=100)


class add_equipment_database(models.Model):
  name=models.CharField(max_length=100)
  category=models.CharField(max_length=100)
  count=models.CharField(max_length=100)
  status=models.CharField(max_length=100)  
  photos=models.FileField(upload_to="documents",null=True)


class add_newreservation_database(models.Model):
  unique_id=models.CharField(max_length=100)
  dt_from=models.CharField(max_length=100)
  dt_to=models.CharField(max_length=100)
  payment=models.CharField(max_length=100)
  price=models.CharField(max_length=100)
  security=models.CharField(max_length=100)
  tax=models.CharField(max_length=100)
  deposit=models.CharField(max_length=100)
  total=models.CharField(max_length=100)
  borrow=models.CharField(max_length=100)
  back=models.CharField(max_length=100)
  items=models.CharField(max_length=100)


class add_invoiceconfig_database(models.Model):
  order_no=models.CharField(max_length=100)
  issue_date=models.CharField(max_length=100)
  due_date=models.CharField(max_length=100)
  created=models.CharField(max_length=100)
  total=models.CharField(max_length=100)
  status=models.CharField(max_length=100)



class reg2(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    c_password=models.CharField(max_length=100)
    email_id=models.EmailField()  


class user_drill_database(models.Model):
  quantity=models.CharField(max_length=100)
  start_dt=models.CharField(max_length=100)
  end_dt=models.CharField(max_length=100)



class check_user_drill_database(models.Model):
  quantity=models.CharField(max_length=100)
  start_dt=models.CharField(max_length=100)
  end_dt=models.CharField(max_length=100)
  total=models.CharField(max_length=100)



class user_cart_database(models.Model):
  quantity=models.CharField(max_length=100)
  price=models.CharField(max_length=100)
  borrow=models.CharField(max_length=100)
  back=models.CharField(max_length=100)