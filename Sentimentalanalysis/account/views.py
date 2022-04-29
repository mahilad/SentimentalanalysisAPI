import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .models import Review
from .forms import ReviewForm
queryset= Review.objects.all()

class IndexView(View):
   def get(self, request):
       return render(request, 'account/index.html')


class FeedbackCreateView(View):
    api_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

    api_headers = {
        'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
        'x-rapidapi-key': "72a5523c17msh1824bfcf3ea29f6p1f2ec4jsnfa7b15afa5cb",
        'content-type': "application/x-www-form-urlencoded"
    }

    def get(self, request):
       review_form = ReviewForm(initial={'sentiment_score': -2.0})
       return render(request, 'account/feedback_create.html', {'review_form': review_form})

    def post(self, request):
       review_form = ReviewForm(request.POST)

       if review_form.is_valid():
           review_instance = review_form.save(commit=False)

           text = review_instance.review_body
           payload = {'text': text}

           response = requests.request("POST", self.api_url, data=payload, headers=self.api_headers)

           review_instance.sentiment_score = response.json()['score':0.8]
           review_instance.save()

           messages.success(request, 'Form submission was successful')
           return redirect('review_sent')

       review_form = ReviewForm()
       return render(request, 'account/feedback_create.html', {'review_form': review_form})


class ReviewsListView(ListView):
        template_name = 'account/reviews_list.html'
        context_object_name = 'account/reviews_list.html'
def get_queryset(self):
       return Review.objects.all()

class ReviewDetailsView(DetailView):
   model = Review
   template_name = 'account/review_details.html'