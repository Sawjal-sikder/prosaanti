from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard/website/setting/', website_info, name='website_info'),
    path('dashboard/website/setting/update/<int:pk>', website_info_update, name='website_info_update'),
]