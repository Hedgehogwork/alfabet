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
from form import *
from mysite.models import Simbol, Oboznach, Dess
import codecs
# Create your views here.
# from dictionary.dict.models import Oboznach
import csv

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
        file = settings.STATIC_URL+"obr_angl_slov.txt"
        f = codecs.open("static/obr_angl_slov.txt", "r", encoding='utf-8')
        # models.oboznach - модель со словами
        # tests = """£.s.d. <br>[͵elesʹdi:] <i>n (сокр. от лат. librae, solidi, denarii)</i> <br>1) фунты стерлингов, шиллинги и пенсы <br>2) <i>разг. </i>деньги, богатство <br>to be short of L.s.d. - сидеть без денег <br>a question /a matter/ of L.s.d. - вопрос в деньгах"""
        for line in f:
            d = []
            # делим строку по <br>
            s = re.split('<br>', line)
            # Получаем слово из первой части
            v_en = s[0].encode('utf8')

            # отделяем транскрипцию
            p = re.compile("(\[.*?\])")

            try:
                t_en = p.search(line)
                t_en = t_en.groups()
                t_en = t_en[0].encode('utf8')
            except:
                t_en = "none"

            try:
                # ищем первый </i>
                regex = re.compile("(^.*?</i>)")
                r = regex.match(line)
                # если li есть режем по нему
                if r:
                    tmp_s = re.split('^.*?</i>', line)
                else:
                    # если нет то режим по скобке
                    tmp_s = re.split('^.*?\]', line)
                v_ru1 = tmp_s[1]
            except:
                # если нет то пусто
                v_ru1 = ''

            try:
                # v_ru2_1 = re.split('\d[\.]', v_ru1)
                v_ru2 = re.split('\d[\.]|\d[)]|<br>', v_ru1)
            except:
                v_ru2 = ''

            clean_q = re.compile('<.*?>|(\[.*?\])')
            v_ru2 = [clean_q.sub("", x) for x in v_ru2]

            # получае все что после него

            # v_ru1 = r[2]



            # отсекаем значение из строки они все идут после 2-го br
            # kol = len(s)
            # v_ru1 = s[2:kol]
            # v_ru1 = [x.encode('utf8') for x in v_ru1]

            # чистим значения от цифр со скобками и без
            # def errase(x):
            #     chars = ['1)', '1.','2)', '2.','3)', '3.','4)', '4.','5)', '5.',]
            #     # x = re.sub('[%s]' % ''.join(chars), '', x)
            #     x = re.sub('(\d[\.)])' % ''.join(chars), '', x)
            #     return x
            #

            # чистим значения от цифр со скобками и без
            # pp = re.compile('(\d[\.])')
            # v_ru1 = [pp.sub("", x) for x in v_ru1]


            tmp = re.split('<i>',s[1])

            # transkrip = tmp[0].encode('utf8')
            l_transkrip = len(t_en)
            # udar = re.findall('[ʹ](em|kju:|eks|bi:|ef|ʤei|en|a:|vi:|ci:|ʤi:|kei|es|dablju:|zed|di:|eiʧ|el|pi:|ti:)', transkrip)

            def find(strng, ch):
                index = 0
                while index < len(strng):
                    if strng[index] == ch:
                        return index
                    index = index + 1
                return -1

            n_udar = find(t_en, '\xcd')
            # m = re.search('(?<=abc)def', 'abcdef')
            # m.group(0)
            if t_en[n_udar+1] in ['k', 'b', 'd', 'p', 't'] and n_udar != -1:
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

            #пишем в базу
            try:
                rec = Oboznach.objects.get(text=v_en)
            except Oboznach.DoesNotExist:
                rec = Oboznach(text=v_en, lang='ru',font='лат.',transkrip=t_en, udaren=n_udar,chast_rechi=chast_rechi,used=used,)
                rec.save()


            #пишем в базу

            for x in v_ru2:
                try:
                    p = Dess.objects.get(text=x)
                except Dess.DoesNotExist:
                    # print "Apress isn't in the database yet."
                    if x != '' and x !=' ':
                        recznach = Dess(text=x, lang='ru',sz=rec)
                        recznach.save()

            # writer = csv.writer(open("/home/semyon/myProject/media/some.csv", "wb"), delimiter=';', quoting=csv.QUOTE_MINIMAL, \
            #         quotechar='`', lineterminator='|')
            # writer.writerows([ [v_en, t_en.encode('utf8')])


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
                                    })

class AlfabetView(View):

    """
    This view handles Personal Area login requests.
    """
    def post(self, request):




        return render(request, 'show.html',
                {})

    def get(self, request):

        oboznach = Oboznach.objects.all()
        dess = Dess.objects.all()
        return render(request, 'show.html',
                               {'dess': dess,
                                'oboznach': oboznach,
                                    })

