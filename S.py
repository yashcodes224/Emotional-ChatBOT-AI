#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install google-cloud-core --upgrade


# In[ ]:


#pip install google-api-core==2.17.1 google-auth==2.28.0


# In[ ]:


#pip install google-generativeai==0.3.0


# In[ ]:


#pip install google-ai-generativelanguage==0.4.0


# In[ ]:


import os 
import google.generativeai as genai

GOOGLE = "AIzaSyA7JxehThu8RfwP8RHC8FZuynD9hP2FF_0"

genai.configure(api_key=GOOGLE)

generation_config = {
  "temperature": 0.7,
  "top_p": 0.9,
  "top_k": 50,
  "max_output_tokens": 1000,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  }
]


model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


# In[ ]:


import random
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

def get_random_loading_text():
    loading_texts = ["Thinking...", "Pondering...", "Calculating...", "Reflecting..."]
    return random.choice(loading_texts)

class EmotionalSupportAnimalChatbot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            'greeting': ["Hello! I'm {} your emotional support companion.", "Hi there! I'm {}.", "Hey! I'm {}!"],
            'comfort': ["I'm here to provide comfort and support.", "You're not alone. I'm here for you.", "Feel free to share your thoughts with me."],
            'encouragement': [
                "You're doing great!",
                "Remember, each day is a new opportunity.",
                "I believe in you!",
                "You have the strength to overcome any challenge.",
                "Your effort is making a difference. Keep going!",
                "Take small steps every day, and progress will follow.",
                "Your journey is unique, and you're making it extraordinary.",
                "You're resilient, and you'll emerge stronger from tough times.",
                "Don't forget to celebrate your achievements, no matter how small."
            ],
            'farewell': ["Take care! Reach out whenever you need.", "Goodbye for now! I'll be here whenever you want to chat.", "Remember, I'm just a message away."],
            'daily_check_in': ["How was your day today?", "I hope your day went well. Anything you'd like to share?", "I'm here to listen. How was your day?"]
        }

    def get_response(self, category):
        return random.choice(self.responses[category])

    def start_conversation(self):
        return self.get_response('greeting').format(self.name) + "\n" + self.get_response('comfort')

    def generate_airesponse(self, prompt):
        prompt_parts = (prompt)
        response = model.generate_content(prompt_parts)
        return response.text

    def daily_check_in(self, user_input):
        prompt = random.choice(self.responses['daily_check_in'])
        return f"{prompt}\nUser: {user_input}\nBot: " + self.generate_airesponse(user_input)
        
    def chat_loop(self, user_input):
        if 'Bye' in user_input:
            return self.get_response('farewell')
        elif 'Encourage' in user_input:
            return self.get_response('encouragement')
        elif 'Daily-check' in user_input:
            return self.daily_check_in(user_input)
        elif 'Who-created-you' in user_input:
                st.write(" My Master's name is Adarsh Singh.")
        else:
            return self.generate_airesponse(user_input)


def main():
    
    def load_lottiefile(filepath: str):
        with open(filepath, "r",encoding='utf-8') as f:
            return json.load(f)
    
    lottieai = load_lottiefile("AI.json")
    
    lottiecoffee = load_lottiefile("coffee.json")
    
    lottieload = load_lottiefile("Chatload.json")
    
    st_lottie(lottieai,speed=4,key="ai", height=500, width=500)
    
    #st_lottie(lottiecoffee,speed=2,key="coffee", height=500, width=500)
    
    st.title("Emotional Support Animal Chatbot")

    # Get user's bot name
    bot_name = st.text_input("Enter your bot name:")

    # Create an instance of the EmotionalSupportAnimalChatbot
    esa_bot = EmotionalSupportAnimalChatbot(bot_name)

    # Start the chat loop
    st.write(esa_bot.start_conversation())

    # User input
    user_input = st.text_input("You:")
    
    if st.button("Send"):
        bot_response=None
        with st.spinner(text=get_random_loading_text()):
            while( bot_response is None):
                #st.lottie(lottieload, speed=2, key="load", height=100, width=100)
                bot_response = esa_bot.chat_loop(user_input)
                if bot_response is not None:
                    break
                
            
        st.write(bot_response)


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




