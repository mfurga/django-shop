from rest_framework import routers
from ads.api import AdsViewSet


router = routers.DefaultRouter()

router.register(r'ads', AdsViewSet)
