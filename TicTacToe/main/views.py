from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<h4>About</h4>")
def start(request):
    # your function code here
    return JsonResponse({"message": "Function Executed"})