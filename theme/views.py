from rest_framework import generics

from .models import Artwork
from .serializers import ArtworkSerializer


class ListArtwork(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class DetailArtwork(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


