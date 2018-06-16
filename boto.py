"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    message =[]
    animations = ["afraid", "bored", "crying", "dancing","dog","giggling", "heartbroke", "money", "take off"]
    extra_msgs = ["You are asking something I suppose?", "I am feeling sleepy now", "Need to take a break","I am going to play with my pet", "see you later"]
    user_message = request.POST.get('msg')
    message = greetcheck(user_message)
    if(not(message)):
        #message=["no", "inlove"]
        message = swearcheck(user_message)
        if(not(message)):
           message = checkexclaim(user_message)
           if(not(message)):
               message = checkquestion(user_message)
               if(not(message)):
                   message = bye(user_message)
                   if(not(message)):
                       
                       message = [random.choice(animations), random.choice(extra_msgs)]

                       
    return json.dumps({"animation":message[0] , "msg": message[1]})


def greetcheck(msg):
    greeting_keywords = ("hello", "hi", "greetings", "sup", "what's up",)
    greeting_responses = ["'hey", "Hi", "Hello", "All good"]
    response =[]
    if(any(n in msg.lower() for n in greeting_keywords)):
        response.append("inlove")
        response.append(random.choice(greeting_responses))
        return response
    else:
        return False
    
def swearcheck(msg):
    swear_words = ("crap", "bloody", "bugger", "cow","minger","idiot", "fool", "moron")
    swear_response = "No swear words please..."
    response=[]
    if(any(n in msg.lower() for n in swear_words)):
       response.append("No")
       response.append(swear_response)
       return response
    else:
        return False
    
def checkexclaim(msg):
    response=[]
    if(msg.endswith("!")):
        response.append("excited")
        response.append("It was surprising")
        return response
    else:
        return False
    
def checkquestion(msg):
    answers = ["It is a difficult question", "I think I can't answer it", "Still thinking for the answer", "It's not my cup of tea"]
    response=[]
    if(msg.endswith("?")):
        response.append("confused")
        response.append(random.choice(answers))
        return response
    else:
        return False

def bye(msg):
    byes = ["bye", "Good bye", "see you later", "go to sleep", "good night"]
    answers = ["Ok, Good Bye see you", "See you later then", "Will wait for you good bye"]
    response=[]
    if(any(n in msg.lower() for n in byes)):
        response.append("ok")
        response.append(random.choice(answers))
        return response
    else:
        return False

@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
