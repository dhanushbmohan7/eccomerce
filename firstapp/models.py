from django.db import models
class Users(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True,default=False)
    username=models.CharField(max_length=50,default=True)
    password=models.CharField(max_length=50,null=False,default=True)

    def __str__(self):
        return str(self.name)
categoreis=(('mobiles','MOBILES'),('tablet','TABLET'),('laptop','LAPTOP'))        
class products(models.Model):

    product_name=models.CharField(max_length=50)
    product_description=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_image=models.ImageField(null=True,blank=True,upload_to='media/')
    product_image2=models.ImageField(null=True,blank=True,upload_to='media/')
    product_category=models.CharField(max_length=20,null=True,blank=True,choices=categoreis)
    def __str__(self):
        return '%s %s'%(self.product_name,self.product_price)


class cart_items(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField()
    def __str__(self):
        return str(self.product)
