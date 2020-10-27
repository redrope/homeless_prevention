from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from .views import DashboardView, StartAppView, ContactModelCreate, ContactModelList, ContactModelDetail, ContactModelUpdate, \
                   ContactModelDelete, HPAPPCreate, HPAPPDetail, HPAPPUpdate, FAQView, HousingModelCreate, HousingModelDetail, \
                   HousingModelUpdate, HousingModelDelete,UtilitiesModelCreate, UtilitiesModelDetail, UtilitiesModelUpdate, UtilitiesModelList


app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'index' ),
    #path('dashboard/', login_required(DashboardView.as_view()), name= 'dashboard'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('startapp/', login_required(StartAppView.as_view()), name='startapp'),
    path('contact_create/', login_required(ContactModelCreate.as_view()), name='contact_create' ),
    path('contact_list/', login_required(ContactModelList.as_view()), name='contact_list' ),
    path('contact_detail/<pk>/', login_required(ContactModelDetail.as_view()), name='contact_detail'),
    path('contact_update/<pk>/', login_required(ContactModelUpdate.as_view()), name='contact_update'),
    path('contact_delete/<pk>/', login_required(ContactModelDelete.as_view()), name='contact_delete'),
    path('hpapp_create/', login_required(HPAPPCreate.as_view()), name='hpapp_create' ),
    path('hpapp_detail/<pk>/', login_required(HPAPPDetail.as_view()), name='hpapp_detail'),
    path('hpapp_update/<pk>/', login_required(HPAPPUpdate.as_view()), name='hpapp_update'),
    path('hpapp_faq/', FAQView.as_view(), name='faq'),
    path('housing_create/', login_required(HousingModelCreate.as_view()), name='housing_create' ),
    path('housing_detail/<pk>/', login_required(HousingModelDetail.as_view()), name='housing_detail' ),
    path('housing_update/<pk>/', login_required(HousingModelUpdate.as_view()), name='housing_update' ),
    path('housing_delete/<pk>/', login_required(HousingModelDelete.as_view()), name='housing_delete' ),
    path('utils_create/', login_required(UtilitiesModelCreate.as_view()), name = 'utils_create'),
    path('utils_detail/<pk>/', login_required(UtilitiesModelDetail.as_view()), name = 'utils_detail'),
    path('utils_update/<pk>/', login_required(UtilitiesModelUpdate.as_view()), name = 'utils_detail'),
    path('utils_list/', login_required(UtilitiesModelList.as_view()), name = 'utils_list'),

]
