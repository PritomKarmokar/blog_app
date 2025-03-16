import logging

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from applibs.logging_utils import get_logger

# logger = get_logger(__name__)
logger = logging.getLogger(__name__)  # Automatically gets the module name


@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        logger.info("Attempting to connect to API")
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        logger.info("Attempting to connect to API")
        response = {"message": "Hello, world"}
        return Response(data=response, status=status.HTTP_200_OK)
    