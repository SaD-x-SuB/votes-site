from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Votes, Profile
from django.contrib.auth.models import User
from .forms import VotesFormAdd
import datetime

logger = logging.getLogger(__name__)
def index(request):
    if request.method == "POST":
        usname = request.POST['username']
        user = User.objects.get(username=usname)
        usVotes = str(user.profile.usedVotes)

        # logger.error(usVotes)
        usedVotes = []
        if usVotes != 'none':
            usVotesId=''
            for ch in usVotes:

                if ch != ',':
                    usVotesId+=ch

                else:

                    usedVotes.append(int(usVotesId))
                    usVotesId=''



        id_ans = request.POST['id']

        vote_id = ''
        vote_ans = ''

        for ch in id_ans:
            if (ch.isdigit()):
                vote_id += ch
            else:
                vote_ans += ch

        # logger.error('')
        # logger.error(vote_id)
        # logger.error(usedVotes)
        # bul = (int(vote_id) in usedVotes)
        # logger.error(bul)

        if not((int(vote_id) in usedVotes)) or usVotes == 'none':

         # host = request.body  # получаем адрес сервера
         # user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
         # path = request.path  # получаем запрошенный путь
         #
         #
         # return HttpResponse(f"""
         #        <p>Host: {host}</p>
         #        <p>Path: {path}</p>
         #        <p>User-agent: {user_agent}</p>
         #   """)





            vote = Votes.objects.get(pk=int(vote_id))

             # 'asn':'12';'anse':'33';

            strOfAns = vote.ansvers
            dicts = []
            anses = []
            counts = []
            s = ''
            inte = ''

            # logger.error('ans id = ' + str(id_ans))
            # logger.error('vote ans =' + str(vote_ans))
            # logger.error('')
            # logger.error('vote id = ' + str(vote.id))
            # logger.error('vote title is ' + str(vote.title))
            # logger.error('str of ansVers is' + str(strOfAns))



            for ch in range(0, len(strOfAns)):
                    if strOfAns[ch].isdigit():
                        inte += strOfAns[ch]
                    elif strOfAns[ch].isalpha():
                        s += strOfAns[ch]
                    elif strOfAns[ch] == ';':
                        counts.append(inte)
                        inte = ''
                        dicts.append(dict.fromkeys(anses, int(counts[0])))
                        counts = []
                        anses = []
                    elif strOfAns[ch] == ':':
                        anses.append(s)
                        s = ''

            for dicte in dicts:
                 if vote_ans in dicte.keys():  # проверка, есть ли строка day в кортеже A
                    dicte[vote_ans]+=1
            # logger.error(dicts)

            strOfAns=''

            for el in dicts:
                 for key, value in el.items():

                    # keys = str(el.keys())
                    # key_str=''
                    # for ch in range(0, len(keys)):
                    #     if(keys[ch] == "'"):
                    #         ch+=1
                    #         while keys[ch] != "'":
                    #             key_str += keys[ch]
                    #             ch+=1

                    strOfAns+= '\''
                    strOfAns += str(key)
                    strOfAns += '\''
                    strOfAns += ':'
                    strOfAns += '\''
                    strOfAns+= str(value)
                    strOfAns += '\''
                    strOfAns += ';'

            # logger.error(strOfAns)
            vote.ansvers = strOfAns
            vote.save()
            request.POST.clear

            usedVotes.append(int(vote_id))
            strOfVotes=''
            for var in usedVotes:
                strOfVotes+= (str(var) + ',')

            user.profile.usedVotes = strOfVotes
            user.profile.save()

        else:
            # < li > < a
            # href = "{% url 'login'%}?next={{request.path}}" > Login < / a > < / li >
            return HttpResponse(
                                " <p>You have been voted</p>"
                                "<a href=''>back</a>"
                                )





# --------------------------------------------------------------------------------------------
    content = {
        'data': Votes.objects.all(),
        'answers': [],
        'values_ans': []
    }
    i = 0

    for el in content['data']:
        strOfAns = el.ansvers
        dicts = []
        anses = []
        counts = []
        s = ''
        inte = ''

        dicts.append(el.id)

        for ch in range(0, len(strOfAns)):
            if strOfAns[ch].isdigit():
                inte += strOfAns[ch]
            elif strOfAns[ch].isalpha():
                s += strOfAns[ch]
            elif strOfAns[ch] == ';':
                counts.append(inte)
                inte = ''

                dicts.append(dict.fromkeys(anses, counts))
                counts = []
                anses = []
            elif strOfAns[ch] == ':':
                anses.append(s)
                s = ''
        content['answers'].append(dicts)

    # logger.error(content['answers'])

    con = content['answers']

    for var in con:
        dicts = []
        dicts.append(var[0])
        for el in range(1, len(var)):
            for key, value in var[el].items():
                dicts.append(value)
        content['values_ans'].append(dicts)
    # logger.error(content['answers'])
    # logger.error(content['values_ans'])



    return render(request, 'main/index.html', content)

def prof(request):
    return render(request,'registration/profile.html')
def myVotes(request):
    content = {
        'none': False,
        'data':[],
        'answers': [],
        'values_ans': [],
    }
    i = 0
    username = request.user.username


    user = User.objects.get(username=username)
    usVotes = str(user.profile.createdVotes)

    # logger.error(usVotes)
    createdVotesIds = []
    if usVotes != 'none':
        usVotesId = ''
        for ch in usVotes:

            if ch != ',':
                usVotesId += ch

            else:

                createdVotesIds.append(int(usVotesId))
                usVotesId = ''
    else:
        content['none']=True

    for el in createdVotesIds:
        content['data'].append(Votes.objects.get(pk=el))

    for el in content['data']:
        strOfAns = el.ansvers
        dicts = []
        anses = []
        counts = []
        s = ''
        inte = ''

        dicts.append(el.id)

        for ch in range(0, len(strOfAns)):
            if strOfAns[ch].isdigit():
                inte += strOfAns[ch]
            elif strOfAns[ch].isalpha():
                s += strOfAns[ch]
            elif strOfAns[ch] == ';':
                counts.append(inte)
                inte = ''

                dicts.append(dict.fromkeys(anses, counts))
                counts = []
                anses = []
            elif strOfAns[ch] == ':':
                anses.append(s)
                s = ''
        content['answers'].append(dicts)

    # logger.error(content['answers'])

    con = content['answers']

    for var in con:
        dicts = []
        dicts.append(var[0])
        for el in range(1, len(var)):
            for key, value in var[el].items():
                dicts.append(value)
        content['values_ans'].append(dicts)
    return render(request, 'registration/myVotes.html',content)


def create(request):
    if request.method=="POST":

        ansv = request.POST['ansvers']
        logger.error(ansv)
        strOfAns=''
        strOfAns +="'"
        for ch in ansv:

            if(ch!=','):
                strOfAns += ch
            else:
                strOfAns += "'"
                strOfAns += ":'0';'"
        strOfAns += "'"
        strOfAns += ":'0';'"
        strOfAns = strOfAns[0:len(strOfAns)-1]
        logger.error(strOfAns)
        # DATE = date.date.today()
        #  request.POST['date'] = DATE
        # form['date'] = DATE
        logger.error(request.POST)
        # request.POST['ansvers'] = strOfAns
        # request.POST['date'] = datetime.date.today()
        toForm={
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'title':request.POST['title'],
            'text':request.POST['text'],
            'ansvers': strOfAns,
            'date': datetime.date.today()
        }
        form = VotesFormAdd(toForm)
        if(form.is_valid()):
            form.save()




    form = VotesFormAdd
    content ={
        'now_date' : datetime.date.today(),
        'form':form
    }

    return render(request, 'registration/create.html', content)