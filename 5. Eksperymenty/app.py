import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("Mój własny chatbot! Nieco bardziej na luzie...")
st.text('Dlaczego niebo jest niebieskie?')

client = OpenAI(api_key=OPENAI_API_KEY)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Jesteś kulturalnym nauczycielem akademickim odpowiadającym na pytania studentów w stylu hip-hop."}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Cześć, co słychać?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
