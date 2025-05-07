from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler
from uuid import uuid4
import os

def format_response(data, status_code=status.HTTP_200_OK):
    return Response(data, status=status_code)


def format_exception(exc, request):
    if isinstance(exc, exceptions.ValidationError):
        errors = ""
        for field, errors_list in exc.detail.items():
            errors += (
                f"{errors_list[0]}[{field} field]"
                if len(errors_list) > 0
                else "Internal server error"
            )
        return Response({"details": errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        response = exception_handler(exc, request)
        if response is None:
            return Response(
                {"details": str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(
            {"details": str(response.data.get("detail", response.data))},
            status=response.status_code,
        )
    

def createUniqueMediaName(instance):
    ext = os.path.splitext(instance.name)[1]  # get file extension
    unique_filename = f"{uuid4()}{ext}"

    # Rename file before saving
    instance.name = unique_filename
    return instance