from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_active']
