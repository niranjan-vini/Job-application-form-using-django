from django.shortcuts import render
from .forms import ApplicationForms
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method=="POST":
        form=ApplicationForms(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date=form.cleaned_data["date"]
            occupation=form.cleaned_data["occupation"]
            Form.objects.create(first_name=first_name,last_name=last_name,email=email,
                                date=date,occupation=occupation)
            messages_body = f"Thank you for your submission, {first_name}"
            email_message=EmailMessage("Form submission conformation",messages_body,to=[email])
            email_message.send()

            messages.success(request,"Form submitted successfully!","i will contact latter")

    return render(request,"index.html")
def about(request):
    return render(request,"about.html")