from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from textblob import TextBlob
from django.http import HttpResponse
from django.db.models import Avg
import csv


# HOME PAGE (FEEDBACK FORM)
def index(request):
    return render(request, 'index.html')


# SUBMIT FEEDBACK
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        college_name = request.POST['college_name']
        event_name = request.POST['event_name']
        event_date = request.POST['event_date']
        rating = int(request.POST['rating'])
        message = request.POST['message']

        polarity = TextBlob(message).sentiment.polarity
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

        Feedback.objects.create(
            name=name,
            department=department,
            college_name=college_name,
            event_name=event_name,
            event_date=event_date,
            rating=rating,
            message=message,
            sentiment=sentiment
        )

        return redirect('/')


# ADMIN DASHBOARD
def admin_dashboard(request):
    feedbacks = Feedback.objects.all()

    positive = Feedback.objects.filter(sentiment='Positive').count()
    negative = Feedback.objects.filter(sentiment='Negative').count()
    neutral = Feedback.objects.filter(sentiment='Neutral').count()

    avg_rating = round(
        Feedback.objects.aggregate(Avg('rating'))['rating__avg'] or 0, 1
    )

    return render(request, 'admin_dashboard.html', {
        'feedbacks': feedbacks,
        'positive': positive,
        'negative': negative,
        'neutral': neutral,
        'avg_rating': avg_rating
    })


# DELETE FEEDBACK
def delete_feedback(request, id):
    fb = get_object_or_404(Feedback, id=id)
    fb.delete()
    return redirect('/dashboard/')


# EXPORT CSV
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="feedback.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Rating', 'Feedback', 'Sentiment'])

    for fb in Feedback.objects.all():
        writer.writerow([fb.name, fb.rating, fb.message, fb.sentiment])

    return response
