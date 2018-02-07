"""
Simple Python Lambda service that provides simple responses to simple "fact"-like intents.
This file supports the following:
 
Intents supported:
 
  Custom:
	About
	Contact
	Upcoming
 
  Required:
	LaunchRequest (request type that calls launch function)
	AMAZON.HelpIntent (intent that calls help function)
	AMAZON.CancelIntent or AMAZON.StopIntent (intent, both use end function)
 
Note, that as long as you keep your intents in sync with your skill intentSchema, you can
simply update or add intents as functions here and the lambda service will use them.
Intents in your Schema may be mixed case -- this code will convert to lower case.
 
 
"""
 
import sys
import re
import logging
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
 
 
import logging
 
# **************************** CUSTOMIZE BELOW *************************************************
 
# --------------- Your functions that implement your intents ------------------
 
def about():
	return "<speak>Randolph Elementary is an elementary school with grades from pre-kindergarten to fifth grade. This school is a Journey school. This allows the school to embark on wonderful journeys to learn.</speak>"
 
def contact():
	return "<speak>Randolph is located at 1552 Sheppard Town Road, Crozier, VA 23039. For more information visit our website at r e s dot goochland schools dot org. If you need to contact us, call 8 0 4, 5 5 6, 5 3 8 5</speak>"
 
def upcoming():
	return "<speak>Tomorrow is the hundredth day of school! There is a make-up snow day on Monday, the 19th.</speak>"
 
 
# --------------- Primary/Required functions (update as needed) ------------------
 
def launch():
	""" Called when the user launches the skill without specifying what they want
	"""

	return "<speak>Welcome to Randolph Elementary School in Crozier, Virginia. You can say, about, for general information. you can say, contact, to hear our phone number and address, or you can say, upcoming, to hear about upcoming events.</speak>"


def help():
	""" Called when the user asks for help
	"""

	return "<speak>This skill provides some basic information about Randolph Elementary School. You can say about for general information, you can say  contact to hear phone number and address, or you can say upcoming for information on upcoming events. </speak>"
 
 
def end():

	return "<speak.Thank you for asking about Randolph Elementary School. Have a great day! </speak>"
 
 
# ***************************** CUSTOMIZE ABOVE **************************************************
 
# --------------- Helpers that build all of the responses ----------------------
 
def build_speechlet_response(title, output, reprompt_text, should_end_session):

	card_output = re.sub('<[^>]*>', '', output)
   
	return {
    	'outputSpeech': {
        	'type': 'SSML',
        	'ssml': output
    	},
    	'card': {
        	'type': 'Simple',
        	'title': title,
        	'content': card_output
    	},
    	'reprompt': {
        	'outputSpeech': {
            	'type': 'PlainText',
            	'text': reprompt_text
        	}
    	},
    	'shouldEndSession': should_end_session
	}
 
 
def build_response(session_attributes, speechlet_response):
	return {
    	'version': '1.0',
    	'sessionAttributes': session_attributes,
    	'response': speechlet_response
    }
 
 
# Function which delegates the speech output for the response based on the JSON file.
# Simply looking up the intent in the responses map created from the parsed JSON.
#
def on_intent(intent_request, session):
	""" Called when the user specifies an intent for this skill """
 
	logger.info("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
 
	intent = intent_request['intent']
	intent_name = intent_request['intent']['name']
 
	# Dispatch to your skill's intent handlers
	session_attributes = {} # No session attributes needed for simple fact response
	reprompt_text = None # No reprompt text set
	speech_output = ""
	should_end_session = True # Can end session after fact is returned (no additional dialogue)
 
	if intent_name == "launch":
		should_end_session = False # Opening a skill requires the session remain open
	elif intent_name == "AMAZON.HelpIntent":
		should_end_session = False # Asking for help requires the session remain open
		intent_name = 'help'
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		intent_name = 'end'
	else:
		intent_name = intent_name.lower()
 
	# Grab the response specified for the given intent of the JSON by calling
	# the function defined in this module
	speech_output = getattr(sys.modules[__name__], intent_name)()
 
	return build_response(session_attributes, build_speechlet_response
                      	(intent_name,speech_output,reprompt_text,should_end_session))
 
# --------------- Main handler ------------------
 
def lambda_handler(event, context):
	""" Route the incoming request based on type (LaunchRequest, IntentRequest,
	etc.) The JSON body of the request is provided in the event parameter.
	"""
	logger.info("event.session.application.applicationId=" +
		event['session']['application']['applicationId'])
 
	"""
	Uncomment this if statement and populate with your skill's application ID to
	prevent someone else from configuring a skill that sends requests to this
	function.
	"""
	# if (event['session']['application']['applicationId'] !=
	#     	"amzn1.echo-sdk-ams.app.[unique-value-here]"):
	# 	raise ValueError("Invalid Application ID")
 
	# I am injecting a new "intent" type of launch in order to
	# provide the response text for a LaunchRequest
	if event['request']['type'] == "LaunchRequest":
		event['request']['intent'] = { 'name':'launch' }

	return on_intent(event['request'], event['session'])
