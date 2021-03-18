from rest_framework import generics
from .pagination import CustomPagination
from .serializers import (
    FileControlRecordSerializer, RegisterDetailSerializer
)


class FileControlRecordListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FileControlRecordSerializer
    pagination_class = CustomPagination

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.all()


class FileControlRecordRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileControlRecordSerializer

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.all()


class RegisterDetailListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RegisterDetailSerializer
    pagination_class = CustomPagination

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.all()


class RegisterDetailRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RegisterDetailSerializer

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.all()
