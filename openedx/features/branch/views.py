from django.http import JsonResponse
from .models import Branch

def get_all_branch(request):
    data = list(Branch.objects.values())
    return JsonResponse(data, safe = False)

