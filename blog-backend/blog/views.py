from django.shortcuts import render
from rest_framework import generics,permissions
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

class BlogPostListCreateView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    