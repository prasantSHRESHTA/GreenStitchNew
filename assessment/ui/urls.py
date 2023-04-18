from django.urls import path,include

from ui import views

urlpatterns = [

    path('',views.home)
]