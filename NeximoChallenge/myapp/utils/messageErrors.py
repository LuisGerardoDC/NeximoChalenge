from .response import Response

methodNothAllowed = Response(
    message = {'message':'Method not allowed'},
    status = 405,
)