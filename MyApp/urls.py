from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('initiate_call/',views.initiate_call,name="initiate_call"),
    path('initiate_call/',views.process_speech,name="process_speech")
]
