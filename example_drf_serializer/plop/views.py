from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from example_drf_serializer.plop.models import Plop
from example_drf_serializer.plop.serializers import PlopSerializer


class PlopViewSet(viewsets.ModelViewSet):
    queryset = Plop.objects.all()
    serializer_class = PlopSerializer
    permission_classes = [AllowAny]
