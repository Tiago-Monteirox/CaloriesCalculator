from django.shortcuts import  render, redirect

def list_food(request):   
    return render(request, 'tables.html', {})

