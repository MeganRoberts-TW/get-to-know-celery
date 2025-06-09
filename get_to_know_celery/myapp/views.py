from django.shortcuts import render
from .tasks import send_fake_email

def send_email_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        send_fake_email.delay(email)
        return render(request, 'success.html', {'email': email})
    return render(request, 'send_email.html')
