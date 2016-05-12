from django.conf.urls import url, include
from example_drf_serializer.plop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'plop', views.PlopViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
