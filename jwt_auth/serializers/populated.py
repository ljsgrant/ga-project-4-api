from .common import UserSerializer
from sightings.serializers.common import SightingSerializer
from sightings.serializers.populated import UserPopulatedSightingSerializer


class PopulatedUserSerializer(UserSerializer):
    sightings = UserPopulatedSightingSerializer(many=True)
