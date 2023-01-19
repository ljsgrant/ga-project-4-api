from .common import UserSerializer
from sightings.serializers.common import SightingSerializer


class PopulatedUserSerializer(UserSerializer):
    sightings = SightingSerializer(many=True)
