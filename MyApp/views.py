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
    return render(request,"index.html")



def initiate_call(request):
    account_sid = 'ACe6e619c1e110ad4c8dea546308379250'
    auth_token = 'b7b9b1a18689de4715bd731597bcf86f'
    client = Client(account_sid, auth_token)

    to_phone_number = '+917776824564'
    from_phone_number = '+13612734227'

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
    name = request.POST['name']
    age = request.POST['age']
    print("Name is:", name)
    print("Age is:", age)
 
    return HttpResponse("#########")