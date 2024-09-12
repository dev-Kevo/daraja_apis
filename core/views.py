from django.shortcuts import render
from django.contrib import messages
from .api_utils import stkpush

def index(request):
    return render(request, 'core/index.html')

def mpesa_stkpush(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if not phone_number:
            messages.error(request, 'Phonenumber should not be empty')
        refined_number = '254' + phone_number.split('0', 1)[1]

        response = stkpush(refined_number)
        print(request)

    return render(request, 'api/stkpush.html')

def till_balance_query(request):
    return render(request, 'api/tillbalancequery.html')
