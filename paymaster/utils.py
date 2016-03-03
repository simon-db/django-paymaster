# -*- coding: utf-8 -*-

from uuid import uuid4
from datetime import datetime

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from . import settings
from . import logger


def number_generetor(view, form):
    """ Генератор номера платежа (по умолчанию) """
    return u'{:%Y%m%d}-{:08x}'.format(datetime.now(), uuid4().get_fields()[0])


class CSRFExempt(object):
    """ Mixin отключения проверки CSRF ключа """

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CSRFExempt, self).dispatch(*args, **kwargs)
