from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sighting
from .serializers.common import SightingSerializer
from .serializers.populated import PopulatedSightingSerializer
from .serializers.userPopulated import UserPopulatedSightingSerializer
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import json


class SightingListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

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


class SightingDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_sighting(self, pk):
        try:
            return Sighting.objects.get(pk=pk)
        except Sighting.DoesNotExist:
            raise NotFound(detail=f"Can't find sighting with key {pk}")

    def get(self, _request, pk):
        sighting = self.get_sighting(pk=pk)
        serialized_sighting = PopulatedSightingSerializer(sighting)
        return Response(serialized_sighting.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        request.data['owner'] = request.user.id
        sighting_to_edit = self.get_sighting(pk=pk)
        if request.user.id != sighting_to_edit.owner.id:
            return Response({"detail": "Unauthorized, you need to be the sighting owner to do that"}, status=status.HTTP_401_UNAUTHORIZED)
        updated_sighting = SightingSerializer(
            sighting_to_edit, data=request.data)
        try:
            updated_sighting.is_valid()
            updated_sighting.save()
            return Response(updated_sighting.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        sighting_to_delete = self.get_sighting(pk=pk)
        sighting_to_delete.delete()
        return Response({"detail": f"Deleted sighting with key {pk}"}, status=status.HTTP_204_NO_CONTENT)


# class SightingSearchView(APIView):
#     def post(self, request):
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         sightings = Sighting.objects.get(bird_sighted=body['forBirdId'])

#         if body['mySightings']:
#             sightings = sightings.filter(owner=request.user.id)
#         serialized_search_results = UserPopulatedSightingSerializer(
#             sightings, many=True)
#         return Response(serialized_search_results.data)
