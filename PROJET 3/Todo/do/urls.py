from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name = 'acceuil'),
    path('<int:my_id>/update',update,name ='update'),
    
]


