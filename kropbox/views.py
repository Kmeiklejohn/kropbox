from django.shortcuts import render



def error_404(request, execption):
        data = {'text': 'This is a 404 error'}
        return render(request,'error.html', data)

def error_500(request):
        data = {'text': 'This is a 500 error' }
        return render(request,'error.html', data)