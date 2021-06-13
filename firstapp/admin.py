from django.contrib import admin
from.models import products,Users,cart_items

class product(admin.ModelAdmin):
    list_display=('id','product_name','product_description','product_price','product_image','product_image2','product_category')

class user(admin.ModelAdmin):
    list_display=('name','email','username','password')    
class Cart(admin.ModelAdmin):
    list_display=('id','product','quantity','price','user')
admin.site.register(products,product)    
admin.site.register(Users,user)    
admin.site.register(cart_items,Cart)    

