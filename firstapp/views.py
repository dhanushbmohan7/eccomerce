from django.shortcuts import render,redirect
from .models import products,Users,cart_items
from django.contrib.auth import authenticate
import requests
from django.db.models import Sum
from django.contrib.auth import logout
from .forms import *

userFound=False
name=None
res=0

user_id=0
def login(request):
    global userFound
    if request.method =='GET':
        email=request.GET.get('email-address')
        password=request.GET.get('password')
        user=authenticate(email=email,password=password)
       
            
        user=Users.objects.filter(email=email,password=password)
        if user:
            user_details=Users.objects.get(email=email,password=password)

            print('user exists',user_details.name)
            userFound=True
            print(userFound)
          
         
            request.session['name']=user_details.name
            request.session['user_id']=user_details.id
            print(request.session['name'])
            return redirect('index')
        else:
            request.session['name']=None
            userFound=False
            print('user not exists')
                
    return render(request,'login.html')

def signup(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        Users(name=name,username=username,email=email,password=password).save()
        
        
        
    return render(request,'signup.html')    




def index(request):
    
    content=products.objects.all()
    global name
    global user_id
    if userFound==True:
        name=request.session['name']
        user_id=request.session['user_id']
        print('name in index:',name)
    else:
        
        name=None
        print('name not')
        
            
      
   



    return render(request,'index.html',{'content':content,'name':name,'id':user_id})

def cart(request):
    
    
    if userFound == False:
         return redirect('login')
        
        
    else:
        user_id=request.session['user_id']
           
    all_items=products.objects.all()
    total_price=cart_items.objects.all().aggregate(Sum('price'))
   
    if request.method == 'POST':
        quantity=0
        id=request.POST.get('product_id')
        print(id)
        data=products.objects.get(id=id)
        price=data.product_price
        print(data)
        
        user=Users.objects.get(id=user_id)
        cart_items.objects.create(product=data,quantity=quantity+1,price=price,user=user).save()

        total_price=cart_items.objects.all().aggregate(Sum('price'))
        
        print('totoal price:')
        print(total_price['price__sum'])
        

        
       
        
        item=cart_items.objects.all()
       
       
    else:
        item=cart_items.objects.all()
    
        return render(request,'cart.html',{'items':item,'content':all_items,'total_price':total_price['price__sum']})   
     

    return render(request,'cart.html',{'items':item,'content':all_items,'total_price':total_price['price__sum']})    
def delete(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        print(id)  
        data=products.objects.get(id=id)
        print(data)
        cart_items.objects.filter(product=data).delete()
        

    return redirect('cart')
def profile(request,id):
    product_deatils=products.objects.get(id=id)
    user={
            'name':product_deatils.product_name,'image':product_deatils.product_image,'description':product_deatils.product_description,
            'image2':product_deatils.product_image2,'price':product_deatils.product_price,'id':product_deatils.id
        }
    return render(request,'home.html',{'user':user})
def home(request):
    print('home method called')
    if request.method == 'GET':
        print('if condition')
        id=request.GET.get('id')
        print(id)

        product_deatils=products.objects.get(id=id)
        user={
            'name':product_deatils.product_name,'image':product_deatils.product_image,'description':product_deatils.product_description,
            'image2':product_deatils.product_image2,'price':product_deatils.product_price,'id':product_deatils.id
        }
        
        print(user)
    return render(request,'home.html',{'user':user})            
def search(request):
    if request.method =='GET':
        name=request.GET.get('item')
        print(name)
        
        product_deatils=products.objects.get(product_name=name)
        
        user={
            'name':product_deatils.product_name,'image':product_deatils.product_image,'description':product_deatils.product_description,
            'image2':product_deatils.product_image2,'price':product_deatils.product_price
        }

    return render(request,'home.html',{'user':user})
def buy(request):
    print('buy method called')
    if request.method =='POST':
        id=request.POST.get('id')
        print(id)    
        product=products.objects.get(id=id)
        data={
            'name':product.product_name,
            'price':product.product_price,'id':product.id
        }

    return render(request,'checkDemo.html',{'data':data}) 

def confirmed(request): 
    print('confirm method called')
    
    if request.method == 'POST':
        id=request.POST.get('id')
        print(id)
        product=products.objects.get(id=id)
        product_name=product.product_name
        price=product.product_price
        desc=product.product_description
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        print(name,phone)
        message=f"Dear {name} Your Order has been placed . The item {product_name}({desc}) will be delivered by tomorrow.Please pay {price}rs on delivery..Enjoy Enjoy!!"
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f"sender_id=shopkart&message={message}&language=english&route=p&numbers={phone}"
        headers = {
        'authorization': "uQhTBbs7FkfARZDyqeIJoPlE0nGpvc41XKNHgMCS5j2m3iYwWLF9G0c8VtZ6kRhumNgiaECrHdJQ41Po",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print('Message sent succesfully')
        print(message)
        if id:
            res=1
        else:
            res=0    
       
    return render(request,'confirmed.html')    

def logout_user(request):

    logout(request)
    
    return redirect('login')  


def base_layout(request):
	template='new.html'
	return render(request,template)    

def buy_cart(request):
    data=cart_items.objects.all()
    total_price=cart_items.objects.all().aggregate(Sum('price'))
    name=request.session['name']
    return render(request,'check2.html',{'data':data,'sum':total_price['price__sum'],'name':name})    

def sell(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('confirmed')
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form' : form})
  
def userProfile(request,id):
    user=Users.objects.get(id=id)
    
    return render(request, 'userProfile.html',{'user':user})  
def categorize(request,category):
    data=products.objects.filter(product_category=category)
    print(data)
    return render(request,'category.html',{'data':data})    
def confirmed_cart(request): 
    print('confirm method called')
    lst=[]
    if request.method == 'POST':
        name=request.POST.get('name')
        
        
        phone=request.POST.get('phone')
        print(name,phone)
        
        products=cart_items.objects.all()
        for i in products:
            lst.append(i.product.product_name)
        message=f"Dear {name} Your Order has been placed . The item {lst} will be delivered by tomorrow.Please pay price rs on delivery..Enjoy Enjoy!!"
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f"sender_id=shopkart&message={message}&language=english&route=p&numbers={phone}"
        headers = {
        'authorization': "uQhTBbs7FkfARZDyqeIJoPlE0nGpvc41XKNHgMCS5j2m3iYwWLF9G0c8VtZ6kRhumNgiaECrHdJQ41Po",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print('Message sent succesfully')
        print(message)
        if id:
            res=1
        else:
            res=0    
       
    return render(request,'confirmed.html')        
def sitemap(request):
    return render(request,'sitemap.xml',content_type = 'text/xml')    
