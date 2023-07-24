#generic template for web based application using openai

import openai
from modules.substitute import *
from flask import Flask, render_template, request

openai.api_key = 'OPENAI KEY HERE'
#Web framework component
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('mywebpage.html') #refer to your webpage htmp file here

#get requests retrieve data from server
#post request upload data to a server for processing and may alter the server state


#@app.route("/get", methods=["GET", "POST"])


#to import another python file in the same directory, or mentioned directory use the syntax: 
# import dir.filename(python file) import *(all) 


#This list sets a context and user inputs are appended here.
messages = []

def main(user_message):
    #main function to set prompt and context
    
    delimiter="####"
    prompt='''Enter your prompt here:
    
    end of prompt'''

    messages = [ {"role": "system", "content": f"{prompt}"}]
    messages.append({"role":"user", "content":f"{delimiter}{user_message}{delimiter}"})
    
    chat= openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature = 0)
    
    #return the message
    return chat.choices[0].message.content


#using flask for web based application

if __name__ == "__main__":
    app.run()
    