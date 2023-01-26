from .common import UserSerializer
from sightings.serializers.common import SightingSerializer
from sightings.serializers.populated import BirdPopulatedSightingSerializer


class PopulatedUserSerializer(UserSerializer):
    sightings = BirdPopulatedSightingSerializer(many=True)
