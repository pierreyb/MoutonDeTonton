from . import models
from . import serializers
from rest_framework import viewsets, permissions


class MoutonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Mouton class"""

    queryset = models.Mouton.objects.all()
    serializer_class = serializers.MoutonSerializer
    permission_classes = [permissions.IsAuthenticated]


class LotViewSet(viewsets.ModelViewSet):
    """ViewSet for the Lot class"""

    queryset = models.Lot.objects.all()
    serializer_class = serializers.LotSerializer
    permission_classes = [permissions.IsAuthenticated]


class TreatmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Treatment class"""

    queryset = models.Treatment.objects.all()
    serializer_class = serializers.TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class LutteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Lutte class"""

    queryset = models.Lutte.objects.all()
    serializer_class = serializers.LutteSerializer
    permission_classes = [permissions.IsAuthenticated]


