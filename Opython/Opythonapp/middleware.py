from django.shortcuts import render

class RequestTrack:
    def __init__(self,view):
        self.view=view
    def __call__(self,request):
        respone =self.view(request)
        return respone

