from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# newly added imports
from django.views import generic
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
# from django.views import generic

# def index(request):
# 	q = Question.objects.all()
# 	return HttpResponse(q)

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
