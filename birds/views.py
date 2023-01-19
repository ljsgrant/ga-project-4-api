from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bird
from .serializers.common import BirdSerializer
from .serializers.populated import PopulatedBirdSerializer
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BirdListView(APIView):
    # This tuple sets the permission levels of specific views
    # by passing in the rest framework authentication class.
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):

        birds = Bird.objects.all()
        serialized_birds = BirdSerializer(birds, many=True)
        return Response(serialized_birds.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id

        bird_to_add = BirdSerializer(data=request.data)
        try:
            bird_to_add.is_valid()
            bird_to_add.save()
            return Response(bird_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as error:
            res = {
                "detail": str(error)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as error:
            return Response({"detail": str(error)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
