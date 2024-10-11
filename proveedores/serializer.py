from rest_framework import serializers
from .models import *

class StockProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model= StockProveedor
        fields='__all__'