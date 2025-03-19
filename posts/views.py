import logging

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

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