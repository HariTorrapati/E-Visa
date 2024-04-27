# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path("", myfunction, name='main'),
    path("about/", myabout, name='about'),
    path("login_view/about/", myabout1, name='about1'),
    path("login/", mylogin, name='login'),
    path("registaration/", myregistration, name='reg'),
    path("contact/", mycontact, name='contact'),
    path("login_view/contact1/", mycontact1, name='contact1'),
    path("adminhome/", adminhome, name='adminpage'),
    path("userhome/", userhome, name='homepage'),
    path("registration_view/", registration_view, name='registration_view'),
    path("login_view/", login_view, name='login_view'),
    path("login_view/topplaces/", show_topplaces, name='show_topplaces'),
    path("login_view/tophotels/", show_tophotels, name='show_tophotels'),
    path("payment", payment, name='payment'),
    path('logout/', logout_view, name='logout'),
    path('submit_visa_application/', submit_visa_application, name='submit_visa_application'),
     #path('submit-visa-application/', views.submit_visa_application, name='submit_visa_application'),
]
