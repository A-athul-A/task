from django.urls import path
from Bankapp import views
urlpatterns = [

    path('',views.home,name='home')
]
