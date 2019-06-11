# from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['hahatext']
    #print(user_text)
    total_count = len(user_text)
    return render(request, 'count.html', {'count': total_count, 'hahatext': user_text})

#统计出现次数的字，还未实现

def about(request):
    return render(request, 'about.html')