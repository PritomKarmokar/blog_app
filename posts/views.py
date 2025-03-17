import logging

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from applibs.logging_utils import get_logger

logger = logging.getLogger(__name__)  # Automatically gets the module name

posts = [
    {
        "id": 1,
        "title": "Why it is difficult to learn and earn",
        "content": "This is to give reasons",
    },
    {
        "id": 2,
        "title": "Learn Python",
        "content": "I don't think it's easy but you can learn if you get proper guidance",
    }
]

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
    

@api_view(http_method_names=["GET"])
def list_posts(request: Request):
    return Response(data=posts, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def post_details(request: Request, post_id: int):
    details = None
    if post_id < 2:
        details = posts[post_id]
    else:
        details = "Not available"
    return Response(data=details, status=status.HTTP_200_OK)