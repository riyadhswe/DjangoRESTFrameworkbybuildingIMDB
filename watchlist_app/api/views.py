from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from watchlist_app.api.serializers import *
from watchlist_app.models import *
from rest_framework.decorators import api_view


# Create your views here.
@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
