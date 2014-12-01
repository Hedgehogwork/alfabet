# -*- coding: utf-8 -*-
import re

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.views.generic.base import View, TemplateView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from uploadapp.form import *
import codecs
# Create your views here.


class UploadAlfabet(View):

    """
    This view handles Personal Area login requests.
    """
    def post(self, request):




        return render(request, 'upload_alfabet.html',
                {})

    def get(self, request):
        gets = 1
        form = UploadFileForm()
        file = settings.STATIC_URL+""
        f = codecs.open("/home/semyon/myProject/alfabet/dictionary/static/en_ru_d.txt", "r", encoding='utf-8')
        # f = codecs.open('unicode.rst', encoding='utf-8')
        # models.oboznach - модель со словами
        tests = """£.s.d. <br>[͵elesʹdi:] <i>n (сокр. от лат. librae, solidi, denarii)</i> <br>1) фунты стерлингов, шиллинги и пенсы <br>2) <i>разг. </i>деньги, богатство <br>to be short of L.s.d. - сидеть без денег <br>a question /a matter/ of L.s.d. - вопрос в деньгах"""
        # tests = """accroach <br>[əʹkrəʋtʃ] <i>v редк.</i> <br>присваивать, узурпировать, незаконно захватывать  """
        d = []
        # prog = re.compile("<br>")
        sss = re.match("<br>",unicode(tests, 'utf-8'))
        s = re.split('<br>',unicode(tests, 'utf-8', errors='ignore'))
        slovo = s[0].encode('utf8')
        kol = len(s)
        znach = s[2:kol]
        # znach = filter(lambda x:x.encode('utf8'), znach)
        # znach = lambda znach:znach.encode('utf8')
        znach = [x.encode('utf-8') for x in znach]
        tmp = re.split('<i>',s[1])
        transkrip = tmp[0].encode('utf8')
        udar = re.findall('[ʹ](em|kju:|eks|bi:|ef|ʤei|en|a:|vi:|ci:|ʤi:|kei|es|dablju:|zed|di:|eiʧ|el|pi:|ti:)', transkrip)

        pattern = 'n(.+)</i>'
        try:
            used = re.findall(pattern, tmp[1])
            used = used[0].encode('utf8')
        except:
            used = '-'
        tmp = re.split(' ',tmp[1])
        chast_rechi = tmp[0].encode('utf8')
        # pattern = '?1)(.+)'
        # znach = re.match(pattern, tests)

        if chast_rechi == "n":
            chast_rechi = 'noun'
        elif chast_rechi == "a":
            chast_rechi = 'adjective'
        elif chast_rechi == "v":
            chast_rechi = 'verb'
        elif chast_rechi == "adv":
            chast_rechi = 'adverb'
        elif chast_rechi == "cj":
            chast_rechi = 'conjunction'
        elif chast_rechi == "prep":
            chast_rechi = 'preposition'
        else:
            chast_rechi = '-'



        id = 0
        # for line in f:
        #     sssss['str'] = re.split('<br>',line)
        #     sssss['str'][0] = вставлякм в базу oboznach  в ячейку text
        #     sssss['str'][1] = вставлякм в базу oboznach  в ячейку transkrip
        #     sssss['str'][1] = udaren нужно проавсить транскрипцию чтобы узнать номер гласной для этого ищем опостроф и потом первую попавшуюся гласную после него
        #     sssss['str'][2] = chast_rechi там сразу после тега <i> идет обознаение n = noun=существительное «a» это adjective=прилагательное, «v» это verb=глагол, «adv» это adverb=наречие, «cj» это conjunction=союз, «prep» это preposition=предлог
        #     sssss['str'][2] = used нужно удалить <i> и обозначение чатси речи и это поместить в ячейку использование
        #     id = id + 1

        return render(request, 'upload_alfabet.html',
                               {'gets': gets,
                               # 'form': form,
                               'f': f,
                               'd': d,
                               's': s,
                               'tests': tests,
                               'slovo': slovo,
                               'transkrip': transkrip,
                               'chast_rechi': chast_rechi,
                               'used': used,
                               'znach': znach,
                               'udar': udar,
                                })

