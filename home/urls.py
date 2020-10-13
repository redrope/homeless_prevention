from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from .views import DashboardView, ContactModelCreate, ContactModelList, ContactModelDetail, ContactModelUpdate, \
                   ContactModelDelete, HPAPPCreate, HPAPPDetail, HPAPPUpdate


app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'index' ),
    #path('dashboard/', login_required(DashboardView.as_view()), name= 'dashboard'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('contact_create/', login_required(ContactModelCreate.as_view()), name='contact_create' ),
    path('contact_list/', login_required(ContactModelList.as_view()), name='contact_list' ),
    path('contact_detail/<pk>/', login_required(ContactModelDetail.as_view()), name='contact_detail'),
    path('contact_update/<pk>/', login_required(ContactModelUpdate.as_view()), name='contact_update'),
    path('contact_delete/<pk>/', login_required(ContactModelDelete.as_view()), name='contact_delete'),
    path('hpapp_create/', login_required(HPAPPCreate.as_view()), name='hpapp_create' ),
    path('hpapp_detail/<pk>/', login_required(HPAPPDetail.as_view()), name='hpapp_detail'),
    path('hpapp_update/<pk>/', login_required(HPAPPUpdate.as_view()), name='hpapp_update'),
]
