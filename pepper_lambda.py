import boto3
import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
pepperCommandTable = dynamodb.Table('PepperCommands')

def insertCommandIntoTable(command, location):
    now = datetime.datetime.utcnow()
    date = str(now.date())
    timestamp = str(now.time())
    try:
        response = pepperCommandTable.put_item(
           Item={
                'date' : date,
                'timestamp' : timestamp,
                'command' : command,
                'location' : location
                }
        )
    except Exception, e:
        print (e) 

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)

def on_launch(event, context):
    return statement("Welcome to the Pepper Controller", "Please tell me a command to give to Pepper.")
    
def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents

    if intent == "GoTo":
        return go_to_intent(event, context)

    # Required Intents

    if intent == "AMAZON.CancelIntent":
        return cancel_intent()

    if intent == "AMAZON.HelpIntent":
        return help_intent()

    if intent == "AMAZON.StopIntent":
        return stop_intent()
            
def go_to_intent(event, context):
    intent = event['request']['intent']
    command = intent['name']
    location = intent['slots']['location']['value']
    insertCommandIntoTable(command, location)
    return statement("GoTo", "Ok, I will tell Pepper to go to the " + location + ".")  

def continue_dialog():
    message = {}
    message['shouldEndSession'] = False
    message['directives'] = [{'type': 'Dialog.Delegate'}]
    return build_response(message)
        
def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)
    
def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech

def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card        

def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response