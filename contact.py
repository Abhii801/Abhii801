from twilio.rest import Client 
 
account_sid = 'ACe9fbb12fe053183a62e90f193192c79f' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG7c240d5980a1411a52f90abfae44a16c', 
                              body='Someone saw your github profile and wants to conatct you',      
                              to='+917666465449' 
                          ) 
 
print(message.sid)
