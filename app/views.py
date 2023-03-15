from django.shortcuts import render
def hai(request):
    return render(request,'hai.html')

# Create your views here.
def bye(request):
    return render(request,'bye.html')