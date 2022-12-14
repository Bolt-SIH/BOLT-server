from drf_yasg2 import openapi

UNAUTHORIZED = openapi.Response("Unauthorized")
SUCCESSFUL = openapi.Response("Successful Request")
UNPROCESSABLE = openapi.Response("Unprocessable Entity")
INTERNAL_SERVER_ERROR = openapi.Response("Internal Server Error")

GET_RESPONSES = {
    200: SUCCESSFUL,
    401: UNAUTHORIZED,
    500: INTERNAL_SERVER_ERROR
}

POST_RESPONSES = {
    200: SUCCESSFUL,
    401: UNAUTHORIZED,
    422: UNPROCESSABLE,
    500: INTERNAL_SERVER_ERROR
}

PUT_RESPONSES = {
    200: SUCCESSFUL,
    401: UNAUTHORIZED,
    422: UNPROCESSABLE,
    500: INTERNAL_SERVER_ERROR
}

DELETE_RESPONSES = {
    200: SUCCESSFUL,
    500: INTERNAL_SERVER_ERROR
}
