from django.conf import settings
from django.contrib.staticfiles.urls import static


from django_tandilHook.urls import path
from . import views

urlpatterns = [

    # SITE -----------------//////////////////////////
    path('', views.home, name='home'),
    path('aboutus/', views.aboutUs, name='aboutus'),
    path('products/', views.products, name='products'),
    path('contactus/', views.contactUs, name='contactus'),
    # SITE -----------------//////////////////////////,
    path('loginhtml/', views.loginhtml, name='loginhtml'),
    path('logout/', views.logoutuser, name='logout'),
    path('registration/', views.createUser, name='signin'),
    # PRODUCTS -----------------//////////////////////////
    path('lures/', views.lures, name='lures'),
    path('clothing/', views.clothing, name='clothing'),
    path('tools/', views.tools, name='tools'),
    #-----------ADD
    path('addlure/', views.addLure, name='addlure'),
    path('addcloth/', views.addCloth, name='addcloth'),
    path('addtool/', views.addTool, name='addtool'),
    #-----------EDIT
    path('editlure/<int:id>', views.editLure, name='editlure'),
    path('editcloth/<int:id>', views.editCloth, name='editcloth'),
    path('edittool/<int:id>', views.editTool, name='edittool'),
    #-----------DELETE
    path('deletelure/<int:id>', views.deleteLure, name='deletelure'),
    path('deletecloth/<int:id>', views.deleteCloth, name='deletecloth'),
    path('deletetool/<int:id>', views.deleteTool, name='deletetool'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)