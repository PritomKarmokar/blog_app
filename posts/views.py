import logging

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView

from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)  # Automatically gets the module name

@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        logger.info("Attempting to connect to API")
        return Response(data=data, status=status.HTTP_201_CREATED)
    else:
        logger.info("Attempting to connect to API")
        response = {"message": "Hello, world"}
        return Response(data=response, status=status.HTTP_200_OK)
    

@api_view(http_method_names=["GET", "POST"])
def list_posts(request: Request):
    
    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Post Created",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            logger.error("Error %s", serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:  
        posts = Post.objects.all()  
        serializer = PostSerializer(instance=posts, many=True)
        data = serializer.data
        response = {
            "message": "posts",
            "data": data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    
@api_view(http_method_names=["GET"])
def post_details(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    if post:
        serializer = PostSerializer(instance=post)
        response = {
            "message": "post",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    # else:
    #     details = {"error": "No post available"}
    #     return Response(data=details, status=status.HTTP_404_NOT_FOUND)

# @api_view(http_method_names=["GET"])
# def get_post_by_id(request: Request):
#     pass

@api_view(http_method_names=["PUT"])
def update_post(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    data = request.data

    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        response = {
            "message": "Post Updated",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        logger.error("Error %s", serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["DELETE"])
def delete_post(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class PostListCreateView(APIView):
    """
        A View for creating and listing posts
    """
    serializer_class = PostSerializer
    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)
        response = {
            "message": "Available Posts",
            "posts": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "New Post created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer

    def get(self, request: Request, post_id: int):
        post = get_object_or_404(Post, pk=post_id)
        
        serializer = self.serializer_class(instance=post)

        response = {
            "message": "Aviable post",
            "data": serializer.data,
        }

        return Response(data=response, status=status.HTTP_200_OK)
        

    def put(self, request: Request, post_id: int):
        data = request.data
        post = get_object_or_404(Post, pk=post_id)

        serializer = self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post Updated",
                "data": serializer.data,
            }

            return Response(data=response, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request: Request, post_id: int):
    #     post = get_object_or_404(Post, pk=post_id)

    #     post.delete()

    #     response = {
    #         "message": f"Post with Id {post_id} deleted successfully",
    #     }

    #     return Response(data=response, status=status.HTTP_204_NO_CONTENT)
        
    """
        Adding ways to handle self error response
    """
    def delete(self, request, post_id: int):
        try:
            post = get_object_or_404(Post, pk=post_id)  # Raises Http404 if not found
            post.delete()
            response = {"message": f"Post with ID {post_id} deleted successfully"}
            return Response(data=response, status=status.HTTP_204_NO_CONTENT)
        
        except Http404:
            response = {"message": f"Post with ID {post_id} not found"}
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        
        