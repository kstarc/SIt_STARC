from django.shortcuts import render


def flex(request):
    return render(request, 'polls/flex.html')


def flex2(request):
    return render(request, 'polls/flex2.html')
