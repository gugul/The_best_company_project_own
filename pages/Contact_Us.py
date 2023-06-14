import streamlit
import pandas

from send_email import send_email

streamlit.header("Contact Us")

with streamlit.form(key="Email form"):
    email_input = streamlit.text_input("Your Email Address")
    label = "What topics do you want to discuss?"
    options = pandas.read_csv("topics.csv")
    select_box = streamlit.selectbox(label, options)
    raw_message = streamlit.text_area("Text")
    message = f"""\
Subject: Mail from {email_input} 

From: {email_input}
{select_box}
{raw_message} 
"""
    button = streamlit.form_submit_button("Submit")
    if button:
        send_email(message)
        streamlit.info("Your email was sent successfully")


