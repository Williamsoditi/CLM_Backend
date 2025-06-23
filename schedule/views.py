from rest_framework import generics
from .models import Schedule, League # Import League model as well if you have a League endpoint
from .serializers import GameSerializer, LeagueSerializer # Import LeagueSerializer if you plan to expose League directly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class GameList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Default permissions

    # Optimize query to fetch related league data in one go (avoids N+1 query problem)
    def get_queryset(self):
        return Schedule.objects.select_related('league').all()

    def get_permissions(self):
        # Admin users can create (POST) new games
        if self.request.method == 'POST':
            return [IsAdminUser()]
        # All other methods (GET for list) are IsAuthenticatedOrReadOnly
        return [IsAuthenticatedOrReadOnly()]

class GameRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Default permissions

    # Optimize query for single object retrieval
    def get_queryset(self):
        return Schedule.objects.select_related('league').all()

    def get_permissions(self):
        # Admin users can update (PUT, PATCH) or delete games
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        # All other methods (GET for retrieve) are IsAuthenticatedOrReadOnly
        return [IsAuthenticatedOrReadOnly()]

# Optionally, if you want an API endpoint for Leagues as well:
class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAdminUser] # Only admins can list/create leagues

class LeagueRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAdminUser] # Only admins can retrieve/update/delete leagues