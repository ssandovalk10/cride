from rest_framework import serializers

class CircleSerializer(serializers.Serializer):
    name=serializers.CharField()
    slug_name=serializers.SlugField()
    rides_taken=serializers.IntegerField()
    rides_offered=serializers.IntegerField()   
    members_limit=serializers.IntegerField()

class CreateCircleSerializer(serializer.Serializer):

    name = serializer.CharField(max_length=140)
    slug_name = serializer.CharField(max_length=40)
    about = serializer.CharField(max_length=255, required=False)
    