from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import LinkChainViewSet


router = SimpleRouter()
router.register(r'links', LinkChainViewSet, basename='link')

urlpatterns = [
    path('', include(router.urls)),
]
