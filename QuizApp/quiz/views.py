from django.shortcuts import render
from .models import Question

# Create your views here.
def quiz_home(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz/quiz_home.html', context)
