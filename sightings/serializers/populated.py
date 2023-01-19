from .common import SightingSerializer
from jwt_auth.serializers.common import UserSerializer
from birds.serializers.populated import PopulatedBirdSerializer
from birds.serializers.common import BirdSerializer


class PopulatedSightingSerializer(SightingSerializer):
    owner = UserSerializer()
    bird_sighted = PopulatedBirdSerializer()


class UserPopulatedSightingSerializer(SightingSerializer):
    bird_sighted = BirdSerializer()
