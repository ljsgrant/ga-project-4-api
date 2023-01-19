from django.urls import path
from .views import BirdListView, BirdDetailView, BirdSearchView, BirdDetailAdminView

urlpatterns = [
    path('', BirdListView.as_view()),
    path('<int:pk>/', BirdDetailView.as_view()),
    path('search/', BirdSearchView.as_view()),
    path('admin/<int:pk>/', BirdDetailAdminView.as_view())
]
