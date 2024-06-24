from django.shortcuts import render, redirect
from InfrastructureCommittee.forms import InfrastructureCommitteeForm
from InfrastructureCommittee.models import InfrastructureCommittee
import inflect
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
    if request.GET.get('project_number') is not None:
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
        id = request.POST.get('id')
        update_infra = InfrastructureCommittee.objects.get(id=id)
        update_infra.abc = request.POST.get('abc', '')
        update_infra.early_procurement = request.POST.get('early_procurement', '')
        update_infra.office = request.POST.get('office', '')
        update_infra.location = request.POST.get('location', '')
        update_infra.calendar_days = request.POST.get('calendar_days', '')
        update_infra.batch = request.POST.get('batch', '')
        update_infra.mode_of_procurement = request.POST.get('mode_of_procurement', '')
        update_infra.pre_bid_date = request.POST.get('pre_bid_date', '')
        update_infra.fund_source = request.POST.get('fund_source', '')
        update_infra.duration = request.POST.get('duration', '')
        update_infra.remarks = request.POST.get('remarks', '')
        update_infra.status = request.POST.get('status', '')
        update_infra.mode = request.POST.get('mode', '')
        update_infra.bid_amount = request.POST.get('bid_amount', '')
        update_infra.pre_proc_date = request.POST.get('pre_proc_date', '')
        update_infra.itb_date = request.POST.get('itb_date', '')
        update_infra.pre_bid_date = request.POST.get('pre_bid_date', '')
        update_infra.bidding_date = request.POST.get('bidding_date', '')
        update_infra.bid_eval_date = request.POST.get('bid_eval_date', '')
        update_infra.post_qua = request.POST.get('post_qua', '')
        update_infra.reso_date = request.POST.get('reso_date', '')
        update_infra.noa_date = request.POST.get('noa_date', '')
        update_infra.contract_date = request.POST.get('contract_date', '')
        update_infra.np_start = request.POST.get('np_start', '')
        update_infra.np_end = request.POST.get('np_end', '')
        
        print(request.POST)
        update_infra.save()
        return redirect(("infrastructure bidding documents"))
    
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