from django.urls import path
from .views import SightingListView

urlpatterns = [
    path('', SightingListView.as_view()),
    # path('<int:pk>/', SightingDetailView.as_view())
]
