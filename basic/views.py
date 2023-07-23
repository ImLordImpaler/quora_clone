from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from .models import * 
from django.contrib.auth.decorators import login_required

@login_required(login_url="login_page")
def homepage(request):
    questions = Question.objects.filter().order_by('-created')
    
    if request.method == "POST":
        question_text = request.POST.get('question_text')
        
        quest = Question.objects.create(
            question_text = question_text , 
            user_id = request.user.id, 
            question_type = 'text'  #implement poll and photo in future
        )
        return redirect('view_question' , quest.id)
    context = {
        'questions': questions
    }
    return render(request , 'index.html', context=context)



@login_required(login_url="login_page")
def view_question(request,pk):
    question = Question.objects.get(id = pk)  
    answers = Answer.objects.filter(question_id = question.id) 
    
    if request.method == 'POST':
        comment = request.POST.get('comment_text')
        Answer.objects.create(
            answer_text = comment , 
            user_id = request.user.id,
            question_id = question.id
        )
        return redirect('view_question', question.id)  
    context = {
        'question': question,
        'answers': answers,
        'upvotes': Reaction.objects.filter(question_id = pk, reaction_type='upvote').count(),
        'downvotes': Reaction.objects.filter(question_id = pk,reaction_type='downvote').count()
    }
    return render(request , "view_question.html", context=context)


def question_react(request, pk, type):
    question = Question.objects.filter(id = pk).values('id')
    if not question:
        return HttpResponse("No Question Found")
    
    reaction_type = 'upvote' if type in [1,'1'] else 'downvote'
    print(reaction_type)
    reaction_obj  =Reaction.objects.filter(user_id = request.user.id , reaction_type = reaction_type, question_id = pk)
    
    if reaction_obj.exists():  # User has already reacted to it. So delete this reaction
        reaction_obj.delete()
        
        
    else:
        reaction_obj = Reaction.objects.create(
            user_id = request.user.id , 
            reaction_type = reaction_type , 
            question_id = pk
        )
    return redirect('view_question', pk)
        
    
    
    