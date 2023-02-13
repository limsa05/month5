from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review
from afisha_api.serializers import ReviewListSeriazer, MovieListSerializer

@api_view(['GET'])
def get_movie(request):
    movie = Movie.objects.all()
    data = MovieListSerializer(movie, many=True).data
    return  Response(data=data)

@api_view(['GET'])
def get_review(request, id):
    try:
        product = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewListSeriazer(product).data
    return Response(data=data)