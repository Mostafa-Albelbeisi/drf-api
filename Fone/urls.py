from django.urls import path
from .views import FoneListView, FoneDetailView

urlpatterns = [
    path("", FoneListView.as_view(), name="fone_list"),
    path("<int:pk>", FoneDetailView.as_view(), name="fone_detail"),
]
