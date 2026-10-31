from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from claims.models import Claim
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClaimForm

def home(request):
    return HttpResponse("Welcome to the Claims Tracker Application")

def claim_list(request):
    claims=Claim.objects.all()
    count=Claim.objects.count()

    for c in claims:
        c.decision_display = c.decision.replace("_"," ").title()

    return render(request, 'claims/claim_list.html', {'claim': claims, 'count': count,})

def claim_detail(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)
    decision_display = claim.decision.replace("_"," ").title() 
    sum_insured_display = f"₹{claim.sum_insured_inr:,}"  # Format sum insured with commas and currency symbol
    return render(request, 'claims/claim_details.html', {'claim': claim, 'decision_display': decision_display, 'sum_insured_display': sum_insured_display})

# def update_decision(request, claim_id):
#     claim = get_object_or_404(Claim, id=claim_id)

#     if request.method == "POST":

#         case_id = request.POST.get('case_id')
#         policy_id = request.POST.get('policy_id')
#         claim_date = request.POST.get('claim_date')
#         sum_insured_inr = int(request.POST.get('sum_insured_inr'))
#         decision = request.POST.get('decision')

#         if decision in ('APPROVED', 'NEEDS_REVIEW', 'REJECTED'):

#             claim.case_id = case_id
#             claim.policy_id = policy_id
#             claim.claim_date = claim_date
#             claim.sum_insured_inr = sum_insured_inr
#             claim.decision = decision

#             claim.save()

#             return redirect('claim_details', claim_id=claim.id)

#         else:
#             error = "Invalid decision."
#             return render(
#                 request,
#                 'claims/claim_update.html',
#                 {'claim': claim, 'error': error}
#             )

#     return render(
#         request,
#         'claims/claim_update.html',
#         {'claim': claim}
#     )




def update_decision(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)

    if request.method == "POST":
        form = ClaimForm(request.POST, instance=claim)

        if form.is_valid():
            form.save()
            return redirect('claim_details', claim_id=claim.id)

    else:
        form = ClaimForm(instance=claim)

    return render(
        request,
        'claims/claim_update.html',
        {'form': form, 'claim': claim}
    )





# def claim_create(request):
#     if request.method ==  'POST':
#         case_id = request.POST.get('case_id')
#         policy_id = request.POST.get('policy_id')
#         claim_date = request.POST.get('claim_date')
#         sum_insured_inr = int(request.POST.get('sum_insured_inr'))
#         decision = request.POST.get('decision')

#         Claim.objects.create(
#             case_id=case_id,
#             policy_id=policy_id,
#             claim_date=claim_date,
#             sum_insured_inr=sum_insured_inr,
#             decision=decision
#         )

#         print(case_id)
#         print(policy_id)
#         print(claim_date)
#         print(sum_insured_inr)
#         print(decision)

#     return render(request, 'claims/claim_create.html')


def claim_create(request):

    if request.method == "POST":

        form = ClaimForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('claim_list')

    else:
        form = ClaimForm()

    return render(
        request,
        'claims/claim_create.html',
        {'form': form}
    )



def delete_claim(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)

    if request.method == "POST":
        claim.delete()
        return redirect('claim_list')

    return render(
        request,
        'claims/claim_confirm_delete.html',
        {'claim': claim}
    )