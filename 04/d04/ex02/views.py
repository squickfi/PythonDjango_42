import logging

from django.conf import settings
from . import forms
from django.shortcuts import render, redirect


def index(request):
    logger = logging.getLogger('history')

    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['your_string'])
        return redirect('/ex02')

    try:
        file = open(settings.HISTORY_LOG_FILE, 'r')
        logs = file.readlines()
        file.close()
    except:
        logs = []

    return render(request, 'ex02/index.html', {'form': forms.History(), 'logs': logs})
