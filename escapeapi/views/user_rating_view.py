from rest_framework import viewsets
from escapeapi.models import UserRating
from escapeapi.serializers import UserRatingSerializer

class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    