from rest_framework import serializers
from .models import FileControlRecord, RegisterDetail


class FileControlRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileControlRecord
        fields = '__all__'


class RegisterDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterDetail
        fields = '__all__'
