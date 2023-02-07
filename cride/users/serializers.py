from rest_framework import serializers
from cride.users.models import User

class UserModelSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.CharField()
    phone_number=serializers.IntegerField()
    is_client=serializers.IntegerField()   
    is_verfied=serializers.IntegerField()

      
        