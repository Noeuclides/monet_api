from django.urls import path

from .views import (
    FileControlRecordListCreateAPIView, FileControlRecordRetrieveUpdateDestroyApiView
)

urlpatterns = [
    path('control/', FileControlRecordListCreateAPIView.as_view(), name='record'),
    path('control/<int:pk>',
         FileControlRecordRetrieveUpdateDestroyApiView.as_view(), name='record_retrieve_update_destroy'),
]