from djoser.serializers import UserSerializer
from rest_framework import serializers
from djoser.serializers import TokenCreateSerializer
from .models import Airplane, Flight, CrewMember, TransitStop, Employee


class CustomTokenCreateSerializer(TokenCreateSerializer):

    def create(self, validated_data):
        token = super().create(validated_data)

        user = self.user
        token['user_id'] = user.id
        token['email'] = user.email

        return token


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'date_joined')


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = '__all__'


class TransitStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitStop
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
