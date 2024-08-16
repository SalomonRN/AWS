from django.urls import path
from .views import *
app_name = "veterinaria"
urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('cita/', cita, name="citas"),
    path('doc/', doctor, name="citas"),
    path('logout/', logout, name='logout'),
    
]
