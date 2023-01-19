from .common import SightingSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedSightingSerializer(SightingSerializer):
    owner = UserSerializer()