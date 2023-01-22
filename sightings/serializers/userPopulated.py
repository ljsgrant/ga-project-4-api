from .common import SightingSerializer
from jwt_auth.serializers.common import UserSerializer


class UserPopulatedSightingSerializer(SightingSerializer):
    owner = UserSerializer()
