from django.urls import path, include
from .views import DesignationListCreateView

urlpatterns = [
    path('designations/', DesignationListCreateView.as_view(), name='designation-list-create'),
]