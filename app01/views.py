# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from django.shortcuts import render, HttpResponse
from django.views import View
from django.conf import settings
import json, hashlib
import logging


logger = logging.getLogger(__name__)


class Handle(View):
    def get(self, request, *args, **kwargs):
        """TOKEN验证"""
        try:
            data = request.GET
            """
            <QueryDict: {u'nonce': [u'4032641489'], u'timestamp': [u'1517829950'], 
            u'echostr': [u'10015944131135553534'], u'signature': [u'da5f64eb248feb6b32e026ea3c705060d635421d']}>

            """
            if not data:
                return HttpResponse('hello, this is handle view')

            logger.info(data)
            signature = data.get('signature')
            timestamp = data.get('timestamp')
            nonce = data.get('nonce')
            echostr = data.get('echostr')
            token = settings.WX_TOKEN

            li = [token, timestamp, nonce]
            li.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()

            if hashcode == signature:
                return echostr
            else:
                return ''

        except Exception, Argument:
            logger.error(Argument)
            return Argument

    def post(self, request, *args, **kwargs):
        pass
