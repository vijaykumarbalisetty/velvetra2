from rest_framework import serializers
from .models import Designer, DesignProject

class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = '__all__'
        # Password can be written but not read back
        extra_kwargs = {'password': {'write_only': False}}

class DesignProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignProject
        fields = '__all__'
