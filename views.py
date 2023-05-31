from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import userForm,Answerform
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Question, Answer, Like,User
from django.db.models import Count
import datetime
s=datetime.datetime.now

def Home(request):

    name = "WELCOME TO HOME"
    return render(request, "trans/home.html", {'name': name})

def register_view(request):
    form=userForm()
    if request.method == 'POST':
    
        form=userForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.error(request,'user created succesfully!!....')
            return redirect('homes')
    return render(request,'trans/register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        name = request.POST['name']
        psw = request.POST['password']
        try:
            user = User.objects.get(user_name=name,password=psw)
            #print(user.Employee_Name)
            request.session['user_name'] = user.user_name
            request.session['password'] = user.password
            request.session['user_Id'] = user.id
            messages.success(request, ("login successful.. !"))
            return redirect('homes')
        except:
            messages.warning(request, ("user not avalable.. !"))
            return redirect('homes')
    return render(request,"trans/login.html")

def logout_view(request):
    request.session.flush()
    messages.success(request, ("Logout successful.. !"))
    return redirect('homes')

def question_list(request):
    if request.session.get("user_Id"):
        emp = Question.objects.all().order_by('-id')
        use=User.objects.all().order_by('-id')
        paginator = Paginator(emp,5)
        page = request.GET.get('pg')
        emp = paginator.get_page(page)
        return render(request, "trans/questionlist.html",{'emp':emp,'use':use})
    else:
        messages.error(request, ("Viwing Questions  not allowed login to see questions"))
        return redirect('homes')
use=0

def view_question(request, pk):
    global use
    if request.session.get("user_Id"):
        username = request.session.get('user_name')

        question = Question.objects.get(id=pk)
        ques = question.question

        if request.method == 'POST':
            answera = request.POST['answer']
            user = User.objects.get(user_name=username)
            use=User.user_name
            answer = Answer.objects.create(user=user, question=question, answer=answera)
            #ans=Allanswers.objects.create(user_name=username,question=ques,answer=answera,created_at=s).save()
            answer.save()
            messages.error(request,'answered to the question succesfully!!!!')
            return redirect('homes')
        
        return render(request, 'trans/Answerquestion.html', {'question': question,'use':use})
    else:
        messages.error(request, 'Login to answer questions')

    

def like_answer(request,answer_id):
    if request.session.get("user_Id"):
        username = request.session.get('user_name')
        answer = Answer.objects.get(pk=answer_id)
        user = User.objects.get(user_name=username)

        try:
            like = Like.objects.get(answer=answer, user=user)
            like.delete()
            messages.error(request, 'You unliked the answer')
        except Like.DoesNotExist:
            cou = Like.objects.filter(answer=answer).count()
            Like.objects.create(answer=answer, user=user, like_count=cou + 1)
            messages.error(request, 'You liked the answer')
        
        return redirect('homes')
    else:
        messages.error(request, 'Login required to like or unlike the answer')
        return redirect('homes')



# Create your views here.
def view_answer(request):
    if request.session.get("user_Id"):
        ans=Answer.objects.all().order_by('-id')
        user=User.objects.all().order_by('-id')
        que=Question.objects.all().order_by('-id')
        
        return render(request,'trans/viewanswer.html',{'user':user,'ans':ans,'que':que})

def post_question(request):
    if request.session.get('user_Id'):
        que = request.POST.get('question')
        username = request.session.get('user_name')
        content = request.POST.get('content')
        
        if que:
            # Retrieve the User instance using the username
            user = User.objects.get(user_name=username)
            
            quest = Question.objects.create(user=user, question=que, content=content)
            quest.save()
            messages.success(request, 'Posted question successfully!')
            return render(request, 'trans/postquestion.html')
        else:
            messages.error(request, 'Question field cannot be empty.')
            return render(request, 'trans/postquestion.html')
    else:
        messages.error(request, 'Cannot post question. Please log in.')
        return redirect('homes')

def view_likes(request):
    if request.session.get('user_Id'):
        lik=Like.objects.all().order_by('-id')
        print(Like.like_count)
        return render(request,'trans/viewlike.html',{'lik':lik})

