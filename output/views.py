from django.shortcuts import render


# def output(request):
#     return render(request, 'output/output.html')

def output(request):
    return render(request, 'output/output_inherited.html')

