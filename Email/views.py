from django.shortcuts import render
from .models import EmailModel
import smtplib,os,sys
# Create your views here.
def home(request):
    data = EmailModel()
    if request.method == 'POST':
        data.Email = request.POST['Email']
        data.Message = request.POST['Message']
        EmailModel.save(data)
        
        
        content = data.Message
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('your Email','password')
        mail.sendmail('your Email',data.Email,content)
        mail.close()
    return render (request,'index.html')
