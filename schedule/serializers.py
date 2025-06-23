from rest_framework import serializers
from .models import League, Schedule

# Serializer for the League model
class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

# Serializer for the Schedule model
class GameSerializer(serializers.ModelSerializer):
    league_name = serializers.CharField(source='league.name', read_only=True)

    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all(), write_only=True)

    class Meta:
        model = Schedule
        # Explicitly list fields for clarity and to include league_name
        fields = [
            'id', # Always good to include the ID
            'game_date',
            'game_time',
            'opponent',
            'location',
            'game_type',
            'league',         # This handles write operations (takes league ID)
            'league_name',    # This handles read operations (displays league name)
        ]