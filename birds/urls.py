from django.urls import path
from .views import BirdListView

urlpatterns = [
    path('', BirdListView.as_view()),
    # path('<int:pk>/', BirdDetailView.as_view()) #
]
