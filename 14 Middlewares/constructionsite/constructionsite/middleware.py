from django.http import HttpResponse
from django.conf import settings
import logging

class UnderConstructionMiddleware:
    """
    Middleware that returns a maintenance page for all requests
    except those from specified IP addresses.
    """
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        if request.path != '/under_constructions/' and settings.SITE_UNDER_CONSTRUCTION:
           return HttpResponse(
                "<html><body><h1>Site Under Maintenance</h1><p>We are currently performing maintenance. Please check back later.</p></body></html>",
                status=503
            )
        response = self.get_response(request)
        return response
    

class FooterAppendMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'text/html' in response.get("Content-Type", ""):
            footer_message = "<footer><p>© 2025 Django Company</p></footer>"
            content = response.content.decode('utf-8')
            content = content.replace("</body>", f"{footer_message}</body>")
            response.content = content.encode('utf-8')
        return response
    
logger = logging.getLogger(__name__)
class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
     

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except ValueError as e:
            logger.error(f"Exception occurred: {e}", exc_info=True)
            return HttpResponse(
                "<html><body><h1>Server Error</h1><p>An unexpected error occurred. Please try again later.</p></body></html>",
                status=500
            )
        except Exception as e:
            logger.error(f"Unhandled Exception: {e}", exc_info=True)
            return HttpResponse(
                "<html><body><h1>Server Error</h1><p>An unexpected error occurred. Please try again later.</p></body></html>",
                status=500
            )
       
      
    