from rest_framework import generics
from .models import Schedule
from .serializers import GameSerializer

class GameList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer