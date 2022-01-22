from pyexpat import model
from django.forms import fields
from rest_framework import serializers
from todo_app.models import List

class ListSerializers(serializers.ModelSerializer):
    class Meta:
        model=List
        fields='__all__'