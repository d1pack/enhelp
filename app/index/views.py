import telebot
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from .models import UserList


class IndexView(TemplateView):
    template_name = 'templates/index/index.html'


def form_handler(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Отправка сообщения в Telegram
        users = UserList.objects.all()
        for user in users:
            try:
                bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
                bot.send_message(user.chat_id,
                                 f"Новая заявка:\n\n"
                                 f"Имя: {name}\n"
                                 f"Телефон: {phone}\n"
                                 f"Email: {email}")
                return HttpResponseRedirect('/')  # Перенаправление на страницу успеха
            except telebot.apihelper.ApiException as e:
                # Обработка ошибок при отправке сообщения
                print(f"Ошибка отправки в Telegram: {e}")