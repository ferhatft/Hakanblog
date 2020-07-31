
from django.shortcuts import render, redirect

from django.contrib import messages
from contact.forms import ContactForm


# Create your views here.


def sorularView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject= form.cleaned_data['subject']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request,'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapılcaktır...')
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, "questions.html",{'form':form})   

