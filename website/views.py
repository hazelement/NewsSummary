from datetime import datetime, timedelta

from django.shortcuts import render


from api.api_models import DailyDigestionAPIModel
from api.dao import DailyDigestionDao



# Create your views here.
def demo(request):
    return render(request, 'website/demo.html')


def index(request):

    start_time = datetime.utcnow() - timedelta(days=1)
    daily_digestions = DailyDigestionDao().get_digestion(start_time)

    return render(request, 'website/index.html', {'site_digestions': daily_digestions})
