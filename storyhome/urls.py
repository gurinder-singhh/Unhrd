from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingpage,name='landingpage'),
    path('user/',views.userhomepage,name='userhomepage'),
    path('profile/',views.profileupdate,name='profileupdate'),
    path('friends/',views.friendslist,name='friendslist'),
    path('addfriend/<int:userid>/',views.addfriends,name='addfriend'),
    path('allusers/',views.getallusers,name='allusers'),
    path('deletefriend/<int:userid>/',views.deletefriends,name='deletefriend'),
]