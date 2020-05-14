from django.shortcuts import render

# Create your views here.
def poem_list(request):
    return render(request, 'talks/talk_list.html')