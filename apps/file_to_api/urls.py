from django.urls import path

from .views import (
    FileControlRecordListCreateAPIView, FileControlRecordRetrieveUpdateDestroyApiView,
    RegisterDetailListCreateAPIView, RegisterDetailRetrieveUpdateDestroyApiView
)

urlpatterns = [
    path('control/', FileControlRecordListCreateAPIView.as_view(), name='record'),
    path('detalle/', RegisterDetailListCreateAPIView.as_view(), name='register_detail'),
    path('control/<int:pk>',
         FileControlRecordRetrieveUpdateDestroyApiView.as_view(), name='record_retrieve_update_destroy'),
    path('detalle/<int:pk>',
         RegisterDetailRetrieveUpdateDestroyApiView.as_view(), name='detail_retrieve_update_destroy'),

]