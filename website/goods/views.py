from django.shortcuts import render

from .models import good


def good_list(request):
    goods = good.objects.all()
    
    context = {
        "goods": goods,
    }
    return render(request, "goods/list.html", context=context)
    