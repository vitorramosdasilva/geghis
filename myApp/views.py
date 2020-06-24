# coding=utf-8
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from myApp.forms import ContatoForm
from django.shortcuts import render


# sendemail/views.py
def indexView(request):
    if request.method == 'GET':
        form = ContatoForm()
        return render(request, "index.html", {'form': form})
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            messages.success(request, 'E-mail enviado com sucesso.\nRetornaremos em até 48 horas úteis.')
            try:
                send_mail(subject, message, email, ['io.vitor.r@gmail.com'])
                form = ContatoForm()
            except BadHeaderError:
                messages.error(request, 'Erro ao enviar e-mail.\nTente Novamente e revise o conteúdo.')
            return render(request, "index.html", {'form': form})
    return render(request, "index.html", {'form': form})


def error_400(request, exception):
    return render(request, '400.html', status=400)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_50x(request, exception):
    return render(request, '500.html', status=500)