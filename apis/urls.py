from django.urls import include, path
from rest_framework import routers
from .views import TesteViewSet


router = routers.DefaultRouter()
router.register(r'', TesteViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]
