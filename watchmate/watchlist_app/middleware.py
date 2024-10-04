from typing import Any
from django.http import HttpResponse

class MyCustomMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):    
        response = self.get_response(request)        
        if isinstance(response, HttpResponse):  # Check if response is an HttpResponse
            user_agent = response.META.get('HTTP_USER_AGENT', 'unknown')  # Use .get() to avoid KeyError
            # You can do something with user_agent here if needed
        return response
    # def __init__(self, get_reponse):
    #     self.get_response = get_reponse
    
    # def __call__(self, request):    
    #     response = self.get_response(request)      
    #     if isinstance(response,HttpResponse):  
    #         response = response.META.get('HTTP_USER_AGENT','unknown')
    #     return response