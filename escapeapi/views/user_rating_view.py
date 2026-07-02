from rest_framework import viewsets
from escapeapi.models import UserRating
from escapeapi.serializers import UserRatingSerializer

class UserRatingViewSet(viewsets.ModelViewSet):
    serializer_class = UserRatingSerializer

    def get_queryset(self): 
        game_ratings = UserRating.objects.all()
        game_id = self.request.query_params.get('game', None)
        if game_id is not None: 
            game_ratings = game_ratings.filter(game=game_id)
        return game_ratings
    