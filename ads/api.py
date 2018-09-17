from rest_framework import viewsets, permissions

from .models import Ad
from .scripts import RequestGETParse
from .serializers import AdsSerializer


class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        ads = Ad.objects.all()
        res = {k: v for k, v in self.request.query_params.items() if v}

        parser = RequestGETParse(ads)
        for k, v in res.items():
            try:
                getattr(parser, k)(v)
            except AttributeError:
                pass
        ads = parser.get_objects()
        return ads
