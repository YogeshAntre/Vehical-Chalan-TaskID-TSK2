from django.urls import path 
from . import views
#from testapp.views import detailsView
from testapp.views import VehicalFormView,VehicalUpdateView,VehicalDetailsView,ChalanFormView,ChalanDetailsView,ChalanUpdateView,RegisterView,loginView,logoutView
urlpatterns=[
    path('vehicles/', views.VehicalDetailsView, name='vehicle_list'),
    path('vehicles/new/', views.VehicalFormView, name='vehicle_create'),
    path('vehicles/<int:pk>/edit/', views.VehicalUpdateView, name='vehicle_edit'),
    path('chalans/', views.ChalanDetailsView, name='chalan_list'),
    path('chalans/new/', views.ChalanFormView, name='chalan_create'),
    path('chalans/edit/<int:pk>/', views.ChalanUpdateView, name='chalan_edit'),
    path('signup/', views.RegisterView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]

   