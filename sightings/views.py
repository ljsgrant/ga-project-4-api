from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sighting
from .serializers.common import SightingSerializer
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SightingListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):

        sightings = Sighting.objects.all()
        serialized_sightings = SightingSerializer(sightings, many=True)
        return Response(serialized_sightings.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id

        sighting_to_add = SightingSerializer(data=request.data)
        try:
            sighting_to_add.is_valid()
            sighting_to_add.save()
            return Response(sighting_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as error:
            res = {
                "detail": str(error)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as error:
            return Response({"detail": str(error)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
