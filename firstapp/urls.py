from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('cart/',views.cart,name='cart'),
    path('delete/',views.delete,name='delete'),
    path('home/',views.home,name='home'),
      path('search/',views.search,name='search'),
      path('buy/',views.buy,name='buy'),
      path('confirmed/',views.confirmed,name='confirmed'),
      path('login/',views.login,name='login'),
      path('signup/',views.signup,name='signup'),
      path('logout/',views.logout_user,name='logout'),
       path('',views.base_layout,name='base_layout'),
       path('buy_cart/',views.buy_cart,name='buy_cart'),
        path('sell/',views.sell,name='sell'),
        path('profile/<id>/',views.profile,name='profile'),
        path('userProfile/<id>/',views.userProfile,name='userProfile'),
        path('categorize/<category>/',views.categorize,name='categorize'),
        path('confirmed_cart/',views.confirmed_cart,name='confirmed_cart'),
        path('sitemap.xml/',views.sitemap,name='sitemap'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
