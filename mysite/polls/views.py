from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from django.shortcuts import get_object_or_404,render
from django.views import generic


# Create your views here.


class IndexView(generic.ListView):
    model =Question
    context_object_name = "latest_question_list"
    template_name = "polls/index.html"
    queryset =Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model =Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model =Question
    template_name = "polls/results.html"

def vote(request:HttpRequest, question_id):
    question= get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(
            "polls/detail.html",
            {
                "question": question,
                "error_massage": "you dint selected_choice"
            },
        )
        
    else:
        selected_choice.votes += 999999999999999999
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
