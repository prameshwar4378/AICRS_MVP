from django.shortcuts import render
import os
from twilio.rest import Client
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method=="POST":
        mobile_no=request.POST.get('txt_mobile_no')
    return render(request,"index.html")



def initiate_call(request):
    account_sid = 'AC8ea66fda4dbf8ff1db096f6987450e14'
    auth_token = '9ff9c9e4a996385c20b9f4886a20c495'
    client = Client(account_sid, auth_token)

    to_phone_number = '+917776824564'
    from_phone_number = '+1 361 273 4227'

    response = VoiceResponse()
    gather = Gather(input='speech', timeout=3, action='/process_speech', method='POST')
    gather.say("what is your claim numbers")
    response.append(gather)

    gather = Gather(input='speech', timeout=3, action='/process_speech', method='POST')
    gather.say("what is your claim resulation")
    response.append(gather)

    call = client.calls.create(
        twiml=str(response),
        to=to_phone_number,
        from_=from_phone_number,
        record=True
    )
    return HttpResponse(f'Call initiated with SID: {call.sid}')


def process_speech(request):
    claim_numbers = request.POST['claim_numbers"']
    claim_resulation = request.POST['claim_resulation']
    print("Claim Numbers:", claim_numbers)
    print("Claim resulation:", claim_resulation)
    return HttpResponse()