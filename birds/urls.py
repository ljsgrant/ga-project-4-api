from django.urls import path
from .views import BirdListView, BirdDetailView, BirdSearchView

urlpatterns = [
    path('', BirdListView.as_view()),
    path('<int:pk>/', BirdDetailView.as_view()),
    path('search/', BirdSearchView.as_view())
]
