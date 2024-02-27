import random
import string
from django.shortcuts import render

def generate_password(length=12, complexity='medium'):
    characters = string.ascii_letters + string.digits + string.punctuation
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        complexity = request.POST.get('complexity', 'medium')
        password = generate_password(length, complexity)
        return render(request, 'password_generator_app/password_generator.html', {'password': password})

    return render(request, 'password_generator_app/password_generator.html')
