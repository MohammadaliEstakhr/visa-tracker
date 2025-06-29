# API endpoints for the AutoFlow application (FastAPI or Django REST style)
from rest_framework import serializers, viewsets
from .models import VisaApplication

class VisaApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaApplication
        fields = '__all__'

class VisaApplicationViewSet(viewsets.ModelViewSet):
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer