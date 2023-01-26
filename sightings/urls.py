from django.urls import path
from .views import SightingListView, SightingDetailView

urlpatterns = [
    path('', SightingListView.as_view()),
    # path('search/', SightingSearchView.as_view()),
    path('<int:pk>/', SightingDetailView.as_view())
]
