from django.shortcuts import render, redirect
from .models import Project, Message
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def portfolio_view(request):
    projects = Project.objects.all()
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = ContactForm(request.POST)    

            if form.is_valid():
                contact_message = form.save()
                
                try:
                    send_mail(
                        f'Subject: {contact_message.subject}',
                        f'Name: {contact_message.full_name}\nEmail: {contact_message.email}\nMessage: {contact_message.message}',
                        settings.DEFAULT_FROM_EMAIL,
                        [settings.CONTACT_EMAIL],
                        fail_silently=False,
                    )
                    return JsonResponse({ 'message': 'Your message has been sent succesfully. You will receive a response shortly!'} ) 
                except Exception as e:
                    return JsonResponse( {'message': 'Failed to send message. Please try again in a few seconds.'})
            else:
                return JsonResponse({'error': form.errors.as_json()}, status=400)
        
        else:
            if form.is_valid():
                contact_message = form.save()
                try:
                    send_mail(
                        f'Portfolio Message: {contact_message.subject}',
                        f'Name: {contact_message.full_name}\nEmail: {contact_message.email}\nMessage: {contact_message.message}',
                        settings.DEFAULT_FROM_EMAIL,
                        [settings.CONTACT_EMAIL],
                        fail_silently=False,
                    )
                    messages.success(request, "Message sent successfully!")
                    return redirect('portfolio')
                except Exception as e:
                    messages.error(request, f"An error occurred while sending email: {e}")
                    return redirect('portfolio')
            else:
                messages.error(request, "Please correct the errors in the form.")
                return redirect('portfolio')
            
    return render(request, 'my_portfolio/portfolio.html', {'projects': projects, 'form': form})
