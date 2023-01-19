from .common import BirdSerializer
from sightings.serializers.common import SightingSerializer


class PopulatedBirdSerializer(BirdSerializer):
    sightings = SightingSerializer(many=True)
