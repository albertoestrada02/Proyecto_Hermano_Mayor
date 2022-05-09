from rest_framework import serializers

from .models import UserT
from .models import Parameter
from .models import Church

class UserTSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserT
        fields = '__all__'

class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = '__all__'

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'