from django.shortcuts import render
from .models import Project, Skill
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    projects = Project.objects.all()
    technical_skills = Skill.objects.filter(category='technical')
    professional_skills = Skill.objects.filter(category='professional')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            form.save()

            # Send email
            send_mail(
                subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                message=f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
            )
            return render(request, 'portfolio_app/index.html', {
                'success': True,
                'projects': projects,
                'technical_skills': technical_skills,
                'professional_skills': professional_skills,
                'form': ContactForm()  # Reset form
            })
    else:
        form = ContactForm()

    return render(request, 'portfolio_app/index.html', {
        'projects': projects,
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'form': form
    })