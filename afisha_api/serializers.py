from rest_framework import serializers
from afisha_api.models import Movie, Review


#
# class CinemaListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cinema
#         fields = 'id name'.split()


class ReviewListSeriazer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description cinema'.split() # genres



