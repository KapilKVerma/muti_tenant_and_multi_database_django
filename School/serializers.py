from rest_framework import serializers
from .models import Student

# Serializing all the fields of Lead Model for JSON


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
 