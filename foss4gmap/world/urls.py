from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ym', views.SuinanjikoViewSet)

urlpatterns = [
    url(r'^$', views.map, name='map'),
    
]
