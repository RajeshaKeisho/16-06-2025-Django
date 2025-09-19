from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormDataForm


def send_email(request):
    subject = "Test Email with HTML and Attachment"
    from_email = "rajarajesha@gmail.com"
    to_email = ["pyweb.rajesha.coding@gmail.com", 'prasadroyal805@gmail.com']

    html_content = render_to_string('email_template.html', {'recipient_name': 'Recipient'})

    email = EmailMultiAlternatives(subject, "This is a test email with HTML content and attachment.", from_email, to_email)
    email.attach_alternative(html_content, "text/html")

    email.extra_headers['X_Mailer'] = "Prasad Royal"

    try:
        email.send()
        return HttpResponse("Congratulation! Email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send email. Error: {str(e)}")
    
def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            attachment = request.FILES['attachment']

            subject = "Form Submission"
            message = "Thank you for submitting the form."
            from_email = "rajarajesha@gmail.com"
            to_email = [email]

            email = EmailMessage(subject, message, from_email, to_email)
            email.attach(attachment.name, attachment.read(), attachment.content_type)

            try:
                email.send()
                return render(request, 'success.html')
            except Exception as e:
                return render(request, 'error.html', {'error': str(e)})
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})