from django.urls import path,include
from watchlist_app.api.views import *

urlpatterns = [
    path('',MovieListAV.as_view(),name='movie_list'),
    path('<int:pk>',MovieDetailAV.as_view(),name='movie_detail'),
]
