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
from dict.models import simbol, Oboznach, Dess_ru
import codecs
# Create your views here.
# from dictionary.dict.models import Oboznach


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

        # models.oboznach - модель со словами
        # tests = """£.s.d. <br>[͵elesʹdi:] <i>n (сокр. от лат. librae, solidi, denarii)</i> <br>1) фунты стерлингов, шиллинги и пенсы <br>2) <i>разг. </i>деньги, богатство <br>to be short of L.s.d. - сидеть без денег <br>a question /a matter/ of L.s.d. - вопрос в деньгах"""
        for line in f:
            d = []
            # sss = re.match("<br>",unicode(line, 'utf-8'))
            s = re.split('<br>',line )
            slovo = s[0].encode('utf8')
            kol = len(s)
            znach = s[2:kol]
            znach = [x.encode('utf8') for x in znach]

            def errase(x):
                chars = ['1)', '1.','2)', '2.','3)', '3.','4)', '4.','5)', '5.',]
                x = re.sub('[%s]' % ''.join(chars), '', x)
                return x

            znach = [errase(x) for x in znach]

            tmp = re.split('<i>',s[1])
            transkrip = tmp[0].encode('utf8')
            l_transkrip = len(transkrip)
            # udar = re.findall('[ʹ](em|kju:|eks|bi:|ef|ʤei|en|a:|vi:|ci:|ʤi:|kei|es|dablju:|zed|di:|eiʧ|el|pi:|ti:)', transkrip)

            def find(strng, ch):
                index = 0
                while index < len(strng):
                    if strng[index] == ch:
                        return index
                    index = index + 1
                return -1

            n_udar = find(transkrip, '\xcd')

            if transkrip[n_udar+1] in ['k', 'b', 'd', 'p', 't'] and n_udar != -1:
                n_udar = n_udar + 2



            pattern = 'n(.+)</i>'
            try:
                used = re.findall(pattern, tmp[1])
                used = used[0].encode('utf8')
            except:
                used = '-'

            try:
                tmp = re.split(' ',tmp[1])
                chast_rechi = tmp[0].encode('utf8')
            except:
                chast_rechi = '-'

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

                # Des_ru


            rec = Oboznach(text=slovo, lang='ru',font='лат.',transkrip=transkrip,udaren=n_udar,chast_rechi=chast_rechi,used=used,)
            rec.save()
            # entry = Oboznach.objects.get(id=1)
            # ttt = Des_ru.objects.get(text='text')


            for x in znach:
                try:
                    p = Dess_ru.objects.get(text=x)
                except Dess_ru.DoesNotExist:
                    # print "Apress isn't in the database yet."
                    recznach = Dess_ru(text=x, lang='ru',)
                    recznach.save()
                # else:
                #     # print "Apress is in the database."
                #     recznach = Dess_ru(text=x, lang='ru',)


                # if x in ttt:
                #     pass
                # else:
                #     recznach = Dess_ru(text=x, lang='ru',)
                #     recznach.save()

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
                               'n_udar': n_udar,
                                })

