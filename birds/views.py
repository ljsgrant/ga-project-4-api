from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bird
from .serializers.common import BirdSerializer
from .serializers.populated import PopulatedBirdSerializer
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class BirdListView(APIView):
    # This tuple sets the permission levels of specific views
    # by passing in the rest framework authentication class.
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):

        birds = Bird.objects.all()
        serialized_birds = BirdSerializer(birds, many=True)
        return Response(serialized_birds.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request.data['owner'] = request.user.id

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


class BirdDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_bird(self, pk):
        try:
            return Bird.objects.get(pk=pk)
        except Bird.DoesNotExist:
            raise NotFound(detail=f"Can't find bird with key {pk}")

    def get(self, _request, pk):
        bird = self.get_bird(pk=pk)
        serialized_bird = PopulatedBirdSerializer(bird)
        return Response(serialized_bird.data, status=status.HTTP_200_OK)


class BirdDetailAdminView(APIView):
    permission_classes = IsAuthenticated and (IsAdminUser, )

    def get_bird(self, pk):
        try:
            return Bird.objects.get(pk=pk)
        except Bird.DoesNotExist:
            raise NotFound(detail=f"Can't find bird with key {pk}")

    def put(self, request, pk):
        bird_to_edit = self.get_bird(pk=pk)
        updated_bird = BirdSerializer(bird_to_edit, data=request.data)
        try:
            updated_bird.is_valid()
            updated_bird.save()
            return Response(updated_bird.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        bird_to_delete = self.get_bird(pk=pk)
        bird_to_delete.delete()
        return Response({"detail": f"Deleted bird with key {pk}"}, status=status.HTTP_204_NO_CONTENT)


class BirdSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('search')
        print(f"searching birds for query: '{search_query}'")
        search_results = Bird.objects.filter(name__icontains=search_query)
        serialized_search_results = BirdSerializer(search_results, many=True)
        return Response(serialized_search_results.data)
