from django.shortcuts import render

def show_html(request):

    return render(request, "checklist/checklist.html")
