from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from ideas.models import User
from .forms import IdeaForm, ProfileForm, LoginForm
from django.core import serializers
from django.forms.models import model_to_dict
from django.urls import reverse
import json
import requests
import social_django
from urllib.parse import unquote, quote
# from social.apps.django_app.default.models import UserSocialAuth


def logged(request):
    cookie=request.META['HTTP_COOKIE']
    # access_token=unquote(cookie.split(";")[4])
    # access_token=(access_token.split(".")[0]).split(":")[1]
    return HttpResponse("Hello, world. You're at the polls index."+ unquote(cookie))


def index(request):
    # identity=social_django.models.UserSocialAuth.objects.get(provider='github')
    # access_token=identity.extra_data['access_token']
    # headers = {'access-token':access_token}
    url="http://localhost:3000/api/org.apache.tvmnetwork.Idea?access_token="+'i4DGtU7ztEnL06mqoiKCyGRYGvOmNxFeqCGUKvatXoTh33uOgvWfME0LRZmf0jDE'
    r=requests.get(url)
    i=r.json()
    latest_user_list = User.objects.all()
    output = ', '.join([q.userid for q in latest_user_list])
    op=""
    # i['owner']=i['owner'].split('#')[1]
    for j in range(0,len(i)):
        i[j]['owner']=i[j]['owner'].split('#')[1]
        # op.append(j['owner'].split('#')[1])
    # return HttpResponse(len(i))
    # return HttpResponse("Hello, world. You're at the polls index."+ " " +output)
    # return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'idea_dashboard.html', {'op':op,'i':i})

def get_historian(request):
    # identity=social_django.models.UserSocialAuth.objects.get(provider='github')
    # access_token=identity.extra_data['access_token']
    # headers = {'access-token':access_token}
    url="http://localhost:3000/api/queries/LookHistorianRecord"
    # url="http://localhost:3000/api/queries/LookTrade"
    r=requests.get(url)
    i=r.json()

    for j in i:
        j['class1']=j.pop('$class')
        j['transactionType']=j['transactionType'].split('.')[-1]
        txn_time= j['transactionTimestamp']
        j['transactionTimestamp']=txn_time.split('T')[0]+" "+txn_time.split('T')[1].split('.')[0]
        # j['transactionId']="<a href=http://localhost:3000/api/queries/Look"+j['transactionType']+"ByTxn?transactionId="+">{{j.CRID}}</a>"
        try:
            j['identityUsed']=j['identityUsed'].split('#')[1]
            j['who']=requests.get('http://localhost:3000/api/system/identities/'+j['identityUsed']).json()['name']
            j['participantInvoking']=j['participantInvoking'].split('#')[1]
        except KeyError:
            print('KeyError')

        # j['0']='http://localhost:3000/api/system/identities/'+j

    # for j in i:
        # op.append(j['owner'].split('#')[1])
    # return HttpResponse(i[0])
    # return HttpResponse("Hello, world. You're at the polls index."+ " " +output)
    # return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'history.html', {'i':i})

def idea(request, idea_id):
    if request.method == 'POST':
        form=IdeaForm(request.POST)
        if form.is_valid():
            # data=request.POST.copy()
            # idea_to_update['class1']="org.apache.tvmnetwork.Idea"
            # idea_to_update['CRID']=data.get('CRID')
            idea=form.save(commit=False)
            a=model_to_dict(idea)
            # a['$class']=a.pop('class1') # org.apache.tvmnetwork.Idea
            a['$class']="org.apache.tvmnetwork.Idea"
            crid=a.pop('CRID',None)
            a.pop('id',None)
            a.pop('class1',None)
            a = {k: " " if v=="" else v for k, v in a.items() }
            op=json.dumps(a)
            opt="Idea updated successfully"
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            API_ENDPOINT="http://localhost:3000/api/org.apache.tvmnetwork.Idea/"+crid
            # a['CRID']
            # a.pop('CRID')
            r = requests.put(url = API_ENDPOINT,headers=headers, data = op)
            if r.status_code==200:
                return HttpResponseRedirect(reverse('index'))
            pastebin_url = r.text
            return HttpResponse(op+" "+pastebin_url)
    url="http://localhost:3000/api/org.apache.tvmnetwork.Idea/"+idea_id
    r=requests.get(url)
    i=r.json()
    user=request
    form = IdeaForm(initial={"class1":"org.apache.tvmnetwork.Idea", "CRID":i['CRID'], "market":i['market'], "plantCode":i['plantCode'], "model":i['model'], "tvmCategory":i['tvmCategory'], "ideaType":i['ideaType'], "partNumber":i['partNumber'], "supplierGSDB":i['supplierGSDB'], "description":i['description'], "ChangeFrom":i['ChangeFrom'], "changeTo":i['changeTo'], "ideaInDate":i['ideaInDate'],  "bcDate":i['bcDate'], "leadFunction":i['leadFunction'], "spoc":i['spoc'], "ideaSource":i['ideaSource'], "CRIDStage":i['CRIDStage'],  "remark":i['remark'], "expImpDate":i['expImpDate'], "weekShownOnImp":i['weekShownOnImp'], "weekShownForProj":i['weekShownForProj'], "annualSavings":i['annualSavings'], "calSaving":i['calSaving'], "carryOverSavings":i['carryOverSavings'], "ageingDays":i['ageingDays'], "rank":i['rank'], "GSR":i['GSR'], "ideaGeneratedBy":i['ideaGeneratedBy'], "dateOfImp":i['dateOfImp'], "owner":i['owner'].split('#')[1]})
    return render(request, 'idea_descr.html', {'form':form,'type': "Idea: "+idea_id, 'action': "Update Idea",'user':user})
    # return HttpResponse("You're looking at idea %s." % idea_id)

def idea_new(request):
    # idea_to_update=Idea()
    if request.method == 'POST':

        form=IdeaForm(request.POST)
        if form.is_valid():
            # data=request.POST.copy()
            # idea_to_update['class1']="org.apache.tvmnetwork.Idea"
            # idea_to_update['CRID']=data.get('CRID')
            idea=form.save(commit=False)
            a=model_to_dict(idea)
            # a['$class']=a.pop('class1')
            a['$class']="org.apache.tvmnetwork.Idea"
            a.pop('id',None)
            a.pop('class1',None)
            a = {k: " " if v=="" else v for k, v in a.items() }
            op=json.dumps(a)
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            API_ENDPOINT="http://localhost:3000/api/org.apache.tvmnetwork.Idea"
            r = requests.post(url = API_ENDPOINT,headers=headers, data = op)
            # extracting response text
            if r.status_code==200:
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse(op)
            # pastebin_url = r.text
            # print("The pastebin URL is:%s"%pastebin_url)
            # serialized_obj=serializers.serialize('json',[idea,])
            # a=serialized_obj[0]
            # struct = json.loads(serialized_obj)
            # data = json.dumps(struct[0])
            # # a=json.loads(serialized_obj)
            # b=data['fields']
            # return HttpResponse(op)
            # return HttpResponse(pastebin_url)
    form = IdeaForm(initial={"class1":"org.apache.tvmnetwork.Idea", "CRID":"", "market":" ", "plantCode":" ", "model":" ", "tvmCategory":" ", "ideaType":" ", "partNumber":" ", "supplierGSDB":" ", "description":" ", "ChangeFrom":" ", "changeTo":" ", "ideaInDate":" ", "bcStatus":" ", "bcDate":" ", "leadFunction":" ", "spoc":" ", "ideaSource":" ", "CRIDStage":" ", "CRIDStatus":" ", "remark":" ", "expImpDate":" ", "weekShownOnImp":" ", "weekShownForProj":" ", "annualSavings":0, "calSaving":0, "carryOverSavings":" ", "ageingDays":0, "rank":" ", "GSR":" ", "ideaGeneratedBy":" ", "dateOfImp":" ", "owner":"resource:org.apache.tvmnetwork.Team#RTM" })
    return render(request, 'idea_descr.html', {'form': form, 'type':"New Idea", 'action': "Create Idea"})

# def profile(request, user_id):
def profile(request):
    if request.method == 'POST':
        form=ProfileForm(request.POST)
        # if form.is_valid():
            # idea=form.save(commit=False)
            # a=model_to_dict(idea)
            # a['$class']=a.pop('class1')
            # a.pop('id',None)
            # a = {k: " " if v=="" else v for k, v in a.items() }
            # op=json.dumps(a)
        headers = {'Content-Type': 'multipart/form-data', 'Accept': 'application/json'}
        API_ENDPOINT="http://localhost:3000/api/wallet/import?access_token=pCYmB602ARXIfvDJqcHgXFQaTQo9bsMZwsruOaU83hJIaIZ8JevAvmnbm8ip70cW"
        op={'card': request.FILES['card_file'], 'name': 'tvm@tvm-network'}
        r = requests.post(url = API_ENDPOINT,headers=headers, data = op)
        pastebin_url = r.text
        # extracting response text
        return HttpResponse(str(request.FILES))
    form = ProfileForm()
    return render(request, 'profile.html', {'form': form, 'type':"Profile Data", 'action': "Update Profile"})
    # response = "You're looking at the profile of %s."
    # return HttpResponse(response % user_id)

def login(request):
    response = "You're looking at the profile of %s."
    form = LoginForm()
    # return HttpResponse(response % user_id)
    return render(request, 'login.html',{'form': form})

def idea_update(request, idea_id):
    if request.method == 'POST':
        form=IdeaForm(request.POST)
        if form.is_valid():
            # data=request.POST.copy()
            # idea_to_update['class1']="org.apache.tvmnetwork.Idea"
            # idea_to_update['CRID']=data.get('CRID')
            idea=form.save(commit=False)
            a=model_to_dict(idea)
            # a['$class']=a.pop('class1') # org.apache.tvmnetwork.Idea
            a['$class']="org.apache.tvmnetwork.Trade"
            a['idea']="resource:org.apache.tvmnetwork.Idea#"+a['CRID']
            a['newOwner']="resource:org.apache.tvmnetwork.Team#"+a.pop('owner',None)
            crid=a.pop('CRID',None)
            a.pop('id',None)
            a.pop('class1',None)
            a = {k: " " if v=="" else v for k, v in a.items() }
            op=json.dumps(a)
            opt="Idea updated successfully"
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            API_ENDPOINT="http://localhost:3000/api/org.apache.tvmnetwork.Trade/"
            # a['CRID']
            # a.pop('CRID')
            r = requests.post(url = API_ENDPOINT,headers=headers, data = op)
            if r.status_code==200:
                return HttpResponseRedirect(reverse('index'))
            pastebin_url = r.text
            return HttpResponse(op+" "+pastebin_url)
    url="http://localhost:3000/api/org.apache.tvmnetwork.Idea/"+idea_id
    r=requests.get(url)
    i=r.json()
    user=request
    form = IdeaForm(initial={"class1":"org.apache.tvmnetwork.Idea", "CRID":i['CRID'], "market":i['market'], "plantCode":i['plantCode'], "model":i['model'], "tvmCategory":i['tvmCategory'], "ideaType":i['ideaType'], "partNumber":i['partNumber'], "supplierGSDB":i['supplierGSDB'], "description":i['description'], "ChangeFrom":i['ChangeFrom'], "changeTo":i['changeTo'], "ideaInDate":i['ideaInDate'],  "bcDate":i['bcDate'], "leadFunction":i['leadFunction'], "spoc":i['spoc'], "ideaSource":i['ideaSource'], "CRIDStage":i['CRIDStage'],  "remark":i['remark'], "expImpDate":i['expImpDate'], "weekShownOnImp":i['weekShownOnImp'], "weekShownForProj":i['weekShownForProj'], "annualSavings":i['annualSavings'], "calSaving":i['calSaving'], "carryOverSavings":i['carryOverSavings'], "ageingDays":i['ageingDays'], "rank":i['rank'], "GSR":i['GSR'], "ideaGeneratedBy":i['ideaGeneratedBy'], "dateOfImp":i['dateOfImp'], "owner":i['owner'].split('#')[1]})
    return render(request, 'idea_descr.html', {'form':form,'type': "Idea: "+idea_id, 'action': "Update Idea",'user':user})
    # return HttpResponse("You're looking at idea %s." % idea_id)

def txn_details(request, txn_id):
    historian_url="http://localhost:3000/api/queries/LookHistorianRecordByTxn?transactionId="+txn_id
    r=requests.get(historian_url)
    i=r.json()
    j=i[0]
    j['transactionType']=j['transactionType'].split('.')[-1]
    txn_type=j['transactionType']
    if txn_type=='UpdateAsset' or txn_type=='AddAsset' or txn_type=='UpdateParticipant' or txn_type=='AddParticipant':
        txn_url="http://localhost:3000/api/queries/Look"+j['transactionType']+"ByTxn?transactionId="+txn_id
        txn_detail=requests.get(txn_url)
        txn_detail_json=txn_detail.json()
        txn_detail_final=txn_detail_json[0]['resources'][0]
    elif txn_type=='ActivateCurrentIdentity' or txn_type=='IssueIdentity':
        txn_url="http://localhost:3000/api/queries/Look"+j['transactionType']+"ByTxn?transactionId="+txn_id
        txn_detail=requests.get(txn_url)
        txn_detail_json=txn_detail.json()
        txn_detail_final=txn_detail_json[0]
    elif txn_type=='Trade':
        txn_url="http://localhost:3000/api/org.apache.tvmnetwork.Trade/"+txn_id
        txn_detail=requests.get(txn_url)
        txn_detail_json=txn_detail.json()
        txn_detail_final=txn_detail_json
    elif txn_type=='StartBusinessNetwork':
        txn_url="http://localhost:3000/api/queries/Look"+j['transactionType']
        txn_detail=requests.get(txn_url)
        txn_detail_json=txn_detail.json()
        txn_detail_final=txn_detail_json[0]['bootstrapTransactions'][0]['resources'][0]
    if txn_type!='Trade':
        # txn_detail_final['transactionId']=j['transactionId']
        txn_detail_final['timestamp']=j['transactionTimestamp']
    return render(request, 'txn_details.html', {'txn_id':txn_id, 'txn_type': j['transactionType'], 'i': txn_detail_final})


def get_idea_history(request, idea_id):

    if request.GET.get('search_box', False):
        idea_id=request.GET.get('search_box', False)
        url="http://localhost:3000/api/queries/LookTradeByIdea?idea=resource%3Aorg.apache.tvmnetwork.Idea%23"+idea_id
        headers = {'Accept': 'application/json'}
        r=requests.get(url)
        i=r.json()
        # m=request.GET["search_box"]
        # m=request.GET.get('search_box', False)
        m=" "
        # for j in i:
        #     j['idea']=j['idea'].split('#')[1]
        #     historian_url="http://localhost:3000/api/queries/LookHistorianRecordByTxn?transactionId="+j['transactionId']
        #     r=requests.get(historian_url)
        #     tn=r.json()
        #     txn=tn[0]
        #     j['participantInvoking']=txn['participantInvoking'].split('#')[1]
        #     j['newOwner']=j['newOwner'].split('#')[1]
            # return render(request, 'idea_history.html', {'i':i, 'idea_id':idea_id, 'm':str(m)})
    else:
            url="http://localhost:3000/api/queries/LookTradeByIdea?idea=resource%3Aorg.apache.tvmnetwork.Idea%23"+idea_id
            headers = {'Accept': 'application/json'}
            r=requests.get(url)
            i=r.json()
            # m=request.GET["search_box"]
            # m=request.GET.get('search_box', False)
            # m="Either the idea does not exist or it is not authorized for the view."
    if len(i)==0:
        m="Either the idea does not exist or it is not authorized for the view."
    else:
        m="Idea: "+idea_id
        for j in i:
            j['idea']=j['idea'].split('#')[1]
            historian_url="http://localhost:3000/api/queries/LookHistorianRecordByTxn?transactionId="+j['transactionId']
            r=requests.get(historian_url)
            tn=r.json()
            txn=tn[0]
            j['participantInvoking']=txn['participantInvoking'].split('#')[1]
            j['newOwner']=j['newOwner'].split('#')[1]
            txn_time= j['timestamp']
            j['timestamp']=txn_time.split('T')[0]+" "+txn_time.split('T')[1].split('.')[0]


    # return HttpResponse(i)
    # return HttpResponse("Hello, world. You're at the polls index."+ " " +output)
    # return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'idea_history.html', {'i':i, 'idea_id':idea_id, 'm':m})


def report(request):
    # access_token=unquote(cookie.split(";")[4])
    # access_token=(access_token.split(".")[0]).split(":")[1]
    return HttpResponse("Hello, world. You're at the report page.")
