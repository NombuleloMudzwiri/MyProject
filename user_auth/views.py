#Imports
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from polls.models import Question, Choice

# Create your views here.

#login athentication
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
    
#disply user
def show_user(request):
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password})

#registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        User.objects.create_user(username=username, password=password, first_name=first_name)
        return redirect('polls:index')
    return render(request, 'registration.html')

#ristrict vote to user only
@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question_id)
    return render(request, 'vote.html', {'question': question})