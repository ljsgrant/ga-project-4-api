from .common import BirdSerializer
from sightings.serializers.userPopulated import UserPopulatedSightingSerializer


class PopulatedBirdSerializer(BirdSerializer):
    sightings = UserPopulatedSightingSerializer(many=True)
