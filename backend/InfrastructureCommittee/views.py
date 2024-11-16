from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.db.utils import IntegrityError 
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from InfrastructureCommittee.forms import InfrastructureCommitteeForm
from InfrastructureCommittee.models import InfrastructureCommittee
import inflect
import json

# Create your views here.

def home(request):
    return render(request, 'InfrastructureCommittee/home.html')

def database(request):
    return render(request, 'InfrastructureCommittee/database.html')

def infra_receiving(request):
    if request.method == "GET": 
        
        return render(request, 'InfrastructureCommittee/infra_receiving.html')
    
    elif request.method == "POST": 
        account_code = request.POST.get('account_code')
        project_number = request.POST.get('project_number')
        project_title = request.POST.get('project_title')
        project_type = request.POST.get('project_type')
        abc = request.POST.get('abc')
        early_procurement = request.POST.get('early_procurement')
        office = request.POST.get('office')
        location = request.POST.get('location')
        calendar_days = request.POST.get('calendar_days')
        batch = request.POST.get('batch')
        mode_of_procurement = request.POST.get('mode_of_procurement')
        pre_bid_date = request.POST.get('pre_bid_date')
        fund_source = request.POST.get('fund_source')
        duration = request.POST.get('duration')
        remarks = request.POST.get('remarks')
        status = request.POST.get('status')
        mode = request.POST.get('mode')
        bid_amount = request.POST.get('bid_amount')
        pre_proc_date = request.POST.get('pre_proc_date')
        itb_date = request.POST.get('itb_date')
        pre_bid_date = request.POST.get('pre_bid_date')
        bidding_date = request.POST.get('bidding_date')
        bid_eval_date = request.POST.get('bid_eval_date')
        post_qua = request.POST.get('post_qua')
        reso_date = request.POST.get('reso_date')
        noa_date = request.POST.get('noa_date')
        contract_date = request.POST.get('contract_date')
        np_start = request.POST.get('np_start')
        np_end = request.POST.get('np_end')
        
        new_receiving = InfrastructureCommittee(account_code=account_code, project_number=project_number, project_title=project_title, project_type=project_type, abc=abc, early_procurement=early_procurement, office=office, location=location, calendar_days=calendar_days, batch=batch, mode_of_procurement=mode_of_procurement, pre_bid_date=pre_bid_date, fund_source=fund_source, duration=duration, remarks=remarks, status=status, mode=mode, bid_amount=bid_amount, pre_proc_date=pre_proc_date, itb_date=itb_date,  bidding_date=bidding_date, bid_eval_date=bid_eval_date, post_qua=post_qua, reso_date=reso_date, noa_date=noa_date, contract_date=contract_date, np_start=np_start, np_end=np_end)
        new_receiving.save()
        return render(request, 'InfrastructureCommittee/infra_receiving.html')

def update_infra(request):
    if request.method == "POST": 
        
        form = InfrastructureCommitteeForm(request.POST, instance = InfrastructureCommittee.objects.get(id=request.POST.get('id')))

        if form.is_valid(): 
            form.save()
            print("Form saved")
            
            return redirect('infrastructure masterlist')
        else: 
            print(form.errors)
            return redirect('infrastructure masterlist')


def bidding_documents(request):
    if request.GET.get('project_number') is not None and request.method == "GET":
        search = request.GET.get('project_number')
        try:
       
            infra_masterlist = InfrastructureCommittee.objects.get(project_number=search)
        
            if infra_masterlist.abc != "None": 
                abc2 = float(infra_masterlist.abc) * 0.02
                abc5 = float(infra_masterlist.abc) * 0.05
                abc_in_words = inflect.engine().number_to_words(infra_masterlist.abc)
            else: 
                abc2 = 0
                abc5 = 0
                abc_in_words = "Zero"
            return render(request, 'InfrastructureCommittee/bidding_documents.html', {'infra': infra_masterlist, 'abc2': abc2, 'abc5': abc5, 
                                                                                      'abc_in_words': abc_in_words})
        except Exception as e: 
            print("No project number found, " + str(e) )
            infra_masterlist = []
            return render(request, 'InfrastructureCommittee/bidding_documents.html')
    
    elif request.method == "POST": 
        form = InfrastructureCommitteeForm(request.POST, instance = InfrastructureCommittee.objects.get(id=request.POST.get('id')))
        form.save()
        try:
       
            infra_masterlist = InfrastructureCommittee.objects.get(project_number=request.POST.get('project_number'))
        
            if infra_masterlist.abc != "None": 
                abc2 = float(infra_masterlist.abc) * 0.02
                abc5 = float(infra_masterlist.abc) * 0.05
                abc_in_words = inflect.engine().number_to_words(infra_masterlist.abc)
            else: 
                abc2 = 0
                abc5 = 0
                abc_in_words = "Zero"
            return render(request, 'InfrastructureCommittee/bidding_documents.html', {'infra': infra_masterlist, 'abc2': abc2, 'abc5': abc5, 
                                                                                      'abc_in_words': abc_in_words})
        except Exception as e: 
            print("No project number found, " + str(e) )
            infra_masterlist = []
            return render(request, 'InfrastructureCommittee/bidding_documents.html')
    
    
    else:
        return render(request, 'InfrastructureCommittee/bidding_documents.html')

def infra_masterlist(request):
    if request.GET.get('project_number') is not None:
        search = request.GET.get('project_number')
        try:
            infra_masterlist = InfrastructureCommittee.objects.get(project_number=search)
            print(infra_masterlist)
            return render(request, 'InfrastructureCommittee/infra_masterlist.html', {'infra': infra_masterlist})
        except Exception as e: 
            infra_masterlist = []
            print("No project number found, " + str(e) )
            return render(request, 'InfrastructureCommittee/infra_masterlist.html')
    else: 

        return render(request, 'InfrastructureCommittee/infra_masterlist.html')

def consultancy_receiving(request):
    return render(request, 'InfrastructureCommittee/consultancy_receiving.html')

@api_view(['GET'])
def getProjectNumbers(request):
    project_numbers = InfrastructureCommittee.objects.all().values('project_number')
    project_numbers = list(project_numbers)
    if project_numbers == []:
        project_numbers = [{}]
        return JsonResponse({'project_numbers': project_numbers}, safe = False)
    else:
        return JsonResponse({'project_numbers': project_numbers}, safe = False)
    
    
@api_view(['POST'])
def addInfraReceiving(request): 
    data = request.body 
    data = data.decode('utf-8')
    json_data = json.loads(data)
    try:
        InfrastructureCommittee.objects.create(
            account_code=json_data.get('account_code', ''), 
            project_number=json_data.get('project_number', ''), 
            project_title=json_data.get('project_title', ''), 
            project_type=json_data.get('project_type', ''), 
            abc=json_data.get('abc', ''), 
            early_procurement=json_data.get('early_procurement', ''), 
            office=json_data.get('office', ''), 
            location=json_data.get('location', ''), 
            calendar_days=json_data.get('calendar_days', ''), 
            batch=json_data.get('batch', ''), 
            mode_of_procurement=json_data.get('mode_of_procurement', ''), 
            pre_bid_date=json_data.get('pre_bid_date', ''), 
            fund_source=json_data.get('fund_source', ''), 
            duration=json_data.get('duration', ''), 
            remarks=json_data.get('remarks', ''), 
            status=json_data.get('status', ''), 
            mode=json_data.get('mode', ''), 
            bid_amount=json_data.get('bid_amount', ''), 
            pre_proc_date=json_data.get('pre_proc_date', ''), 
            itb_date=json_data.get('itb_date', ''), 
            bidding_date=json_data.get('bidding_date', ''), 
            bid_eval_date=json_data.get('bid_eval_date', ''), 
            post_qua=json_data.get('post_qua', ''), 
            reso_date=json_data.get('reso_date', ''), 
            noa_date=json_data.get('noa_date', ''), 
            contract_date=json_data.get('contract_date', ''), 
            np_start=json_data.get('np_start', ''), 
            np_end=json_data.get('np_end', '')
        )
        
    except IntegrityError as e: 
        print(e)
        return JsonResponse({'status': 'error', 'message' : 'Project number already existing in the database.'}, safe = False)
    
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message' : 'Form error.'}, safe = False)
    return JsonResponse({'status': 'success', 'message': 'Project added successfully.'}, safe = False)


@api_view(['POST']) 
def updateInfraMasterlist(request): 
    data = request.body 
    data = data.decode('utf-8') 
    json_data = json.loads(data) 
    print(json_data['project_number'])
    try: 
        InfrastructureCommittee.objects.filter(project_number=json_data['project_number']).update(
            account_code=json_data.get('account_code', ''), 
            project_title=json_data.get('project_title', ''), 
            project_type=json_data.get('project_type', ''), 
            abc=json_data.get('abc', ''), 
            early_procurement=json_data.get('early_procurement', ''), 
            office=json_data.get('office', ''), 
            location=json_data.get('location', ''), 
            calendar_days=json_data.get('calendar_days', ''), 
            batch=json_data.get('batch', ''), 
            mode_of_procurement=json_data.get('mode_of_procurement', ''), 
            pre_bid_date=json_data.get('pre_bid_date', ''), 
            fund_source=json_data.get('fund_source', ''), 
            duration=json_data.get('duration', ''), 
            remarks=json_data.get('remarks', ''), 
            status=json_data.get('status', ''), 
            mode=json_data.get('mode', ''), 
            bid_amount=json_data.get('bid_amount', ''), 
            pre_proc_date=json_data.get('pre_proc_date', ''), 
            itb_date=json_data.get('itb_date', ''), 
            bidding_date=json_data.get('bidding_date', ''), 
            bid_eval_date=json_data.get('bid_eval_date', ''), 
            post_qua=json_data.get('post_qua', ''), 
            reso_date=json_data.get('reso_date', ''), 
            noa_date=json_data.get('noa_date', ''), 
            contract_date=json_data.get('contract_date', ''), 
            np_start=json_data.get('np_start', ''), 
            np_end=json_data.get('np_end', '')
        )
        
    except ObjectDoesNotExist as e: 
        print(e)
        return JsonResponse({'status': 'error', 'message' : 'Project number does not exist.'}, safe = False)
    except Exception as e: 
        print(e)
        return JsonResponse({'status': 'error', 'message' : 'An error has occured.'}, safe = False)
    return JsonResponse({'status': 'success', 'message': 'Project updated successfully.'}, safe = False)


@csrf_exempt
def searchInfraMasterlist(request): 
    if request.method == "POST":
        data = request.body     
        data = data.decode('utf-8') 
        json_data = json.loads(data) 
        
                
        if json_data['project_number'] != '': 
            project_number = json_data['project_number']
            try: 
                receiving = InfrastructureCommittee.objects.get(project_number=project_number)
                fields = ['account_code', 'project_number', 'project_title', 'project_type', 'abc', 'early_procurement', 'office', 'location', 'calendar_days', 'batch', 'mode_of_procurement', 'pre_bid_date', 'fund_source', 'duration', 'remarks', 'status', 'mode', 'bid_amount', 'pre_proc_date', 'itb_date', 'bidding_date', 'bid_eval_date', 'post_qua', 'reso_date', 'noa_date', 'contract_date', 'np_start', 'np_end']
                data = {field: getattr(receiving, field) for field in fields}
                return JsonResponse({'status': 'success', 'data': data}, safe = False)
                
            except ObjectDoesNotExist as e: 
                print(e)
                return JsonResponse({'status': 'success', 'data' : ''}, safe = False)
         

    else: 
        return JsonResponse({'status': 'error', 'message' : 'An error has occured.'}, safe = False)


