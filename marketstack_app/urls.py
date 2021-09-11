
from marketstack_app import views
from marketstack_app.views import tracking_error
from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.tracking_error,name='tracking_error'),
]
