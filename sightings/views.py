from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sighting
from .serializers.common import SightingSerializer 
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
# class SightingListView