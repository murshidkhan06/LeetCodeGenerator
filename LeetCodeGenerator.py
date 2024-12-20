import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")
st.header("Leet code solution generator")
language_option = st.selectbox('In which language do you want your Leet code solution', ('Python','Java','Go','C++','JavaScript','Ruby'))
leetcode_question = st.text_area("Type your leet code problem with constraints")
button = st.button("Fetch code")


def generate_auto_reponse(leetcode_question,language_option):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f""" Give a {language_option} code for the leet code question below 
                Leet Code Question : {leetcode_question} 
                {language_option} Solution :""",
        temperature=0.7,
        max_tokens=1125,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text

if leetcode_question and button and language_option:
  with st.spinner(".......Generating Code to your Leet code Problem........"):
    reply = generate_auto_reponse(leetcode_question,language_option)
    st.write(reply)
