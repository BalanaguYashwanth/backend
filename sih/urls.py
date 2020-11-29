from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('v1',views.datasViewset,basename='v1')

urlpatterns=[
    path('register',views.register.as_view(),name='register'),
    path('login',views.login.as_view(),name='login'),
    path('logout',views.logout.as_view(),name='logout'),
    path('api/',include(router.urls)),
]

