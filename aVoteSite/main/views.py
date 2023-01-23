from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Votes, Profile
from django.contrib.auth.models import User
from .forms import VotesFormAdd
from .forms import default_const
import datetime
from django.views.generic import DetailView, ListView



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
#     content = {
#         'data': Votes.objects.all(),
#         'answers': [],
#         'values_ans': []
#     }
    content = {
        'data': Votes.objects.order_by('-date'),
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

def refactor(request):

    id = request.POST['id']
    content = {
        'data': Votes.objects.get(pk=id),
        'form': 0,
        'answers':''
    }
    vote = Votes.objects.get(pk=int(id))

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
    total_anses=[]
    for ch in range(0, len(strOfAns)):
        if strOfAns[ch].isdigit():
            inte += strOfAns[ch]
        elif strOfAns[ch].isalpha():
            s += strOfAns[ch]
        elif strOfAns[ch] == ';':
            counts.append(inte)
            inte = ''
            dicts.append(dict.fromkeys(anses, int(counts[0])))
            total_anses+=anses
            counts = []
            anses = []
        elif strOfAns[ch] == ':':
            anses.append(s)
            s = ''
    logger.error(total_anses)
    for st in total_anses:
        content['answers'] +=str(st)+","

    content['answers'] = content['answers'][0:len(content['answers'])-1]

    # form.Meta.dfu_02(form.Meta,content['data'].title,content['data'].text,content['data'].ansvers,form.Meta.widgets)




    toForm = {
        'title': content['data'].title,
        'text':content['data'].text,
        'ansvers': content['answers'],
    }
    form = VotesFormAdd(toForm)
    content['form'] = form
    return render(request, 'registration/shit.html', content)


def myVotes(request):
    if request.method == "POST":
        logger.error(str(request.POST)+ "s-----------------------------------------------------------------------1")
        if request.POST['ref_id']=='none':
            return HttpResponse(refactor(request))

        elif request.POST['ref_id']=='delete':
            logger.error(
            str(request.POST) + "s-----------------------------------------------------------------------3")
            id = request.POST['id']
            Vote = Votes.objects.get(pk=id)
            Vote.delete()
            usname = request.POST['username']
            user = User.objects.get(username=usname)
            crVotes = str(user.profile.createdVotes)
            crVotesArr=[]
            hstr=''
            for ch in crVotes:
                if(ch==','):
                    crVotesArr.append(hstr)
                    hstr=''
                else:
                    hstr+=ch
            if id in crVotesArr:
                logger.error(str(request.POST) + "s-----------------------------------------------------------------------4")
                crVotesArr.remove(id)
            crVotes=''
            for el in crVotesArr:
                logger.error(str(el))
                crVotes += str(el) +','
            user.profile.createdVotes = ''
            logger.error(crVotes)
            user.profile.createdVotes = crVotes
            user.profile.save()
            return HttpResponse("<p>deleted</p> <a href = 'myVotes'>back</a>")
        else:
            logger.error(str(request.POST) + "s-----------------------------------------------------------------------2")
            logger.error(request.POST)
            id = request.POST['ref_id']
            Vote = Votes.objects.get(pk=id)
            date = str(Vote.date)

            ansv = request.POST['ansvers']
            logger.error(ansv)
            strOfAns = ''
            strOfAns += "'"
            for ch in ansv:

                if (ch != ','):
                    strOfAns += ch
                else:
                    strOfAns += "'"
                    strOfAns += ":'0';'"
            strOfAns += "'"
            strOfAns += ":'0';'"
            strOfAns = strOfAns[0:len(strOfAns) - 1]

            toForm = {
                     'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                     'title':request.POST['title'],
                     'text':request.POST['text'],
                     'ansvers': strOfAns,
                     'date': date
                 }

            Vote.title = toForm['title']
            Vote.text = toForm['text']
            Vote.ansvers = toForm['ansvers']
            Vote.date = toForm['date']
            Vote.save()

            request.method = 'GET'
            myVotes(request)
            return HttpResponse(refactor(request))
            #     logger.error(some_id)
            # else:

    else:

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
            jst_created = form.save()
            logger.error(jst_created)
            username = request.user.username
            user = User.objects.get(username=username)
            usVotes = str(user.profile.createdVotes)
            if usVotes != 'none':

                for_pk = str(jst_created)
                logger.error(for_pk)

                newVoteId = Votes.objects.get(pk = for_pk)
                # logger.error(user.profile.createdVotes)
                usVotes += str(newVoteId)+","
                user.profile.createdVotes = usVotes
                user.profile.save()
            else:
                usVOtes=''
                newVoteId = Votes.objects.get(title=toForm['title'])
                # logger.error(user.profile.createdVotes)
                usVotes += str(newVoteId) + ","
                user.profile.createdVotes = usVotes
                user.profile.save()

    form = VotesFormAdd
    content ={
        'now_date' : datetime.date.today(),
        'form':form
    }

    return render(request, 'registration/create.html', content)

class VoteDetailView(DetailView):
    model = Votes
    template_name ="registration/detail_view.html"
    context_object_name = 'Vote'
    queryset = Votes.objects.all()



