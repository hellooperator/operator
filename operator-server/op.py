from telapi import rest, inboundxml
import requests

account_sid = 'AC6c8890845673e4b306e74e16990b475d'
auth_token  = 'fc1d521995724225a4d58f661aa732fc'
client      = rest.Client(account_sid, auth_token)
account     = client.accounts[client.account_sid]

def place_call(phone, sequence):
    call  = account.calls.create( 
        from_number = '+16176844744', 
        to_number = phone, 
        url = 'http://happyoperator.com/inbound/connected/'+sequence
    )
    return "success"

def press_buttons(sid, sequence):
    # call  = account.calls[str(sid)]
    # call.play_dtmf = sequence
    # call.save()

    r = requests.post('https://api.telapi.com/v1/Accounts/AC6c8890845673e4b306e74e16990b475d/Calls/'+sid+'.json', auth=(account_sid, auth_token), data={'PlayDtmf': sequence})
    print r.content

    print sequence
    pause_duration = int(len(sequence) * 0.5 + 1)
    return '<?xml version="1.0"?>\n' + str(inboundxml.Response(
        inboundxml.Pause(length=pause_duration)
    ))