import openai
from openai import OpenAI
import streamlit as st

# Stel de OpenAI API-sleutel in
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Maak een client-object
client = OpenAI(api_key=openai.api_key)

st.title('🦜🔗 Fine-tune tester')

def get_model(input_text):
    system_prompt = """Je bent CATja, een vriendelijke behulpzame AI die vragen gedetaileerd (met volledige zinnen) beantwoord van therapeuten (of toekomstige therapeuten) die aangesloten zijn (of zichzelf aan willen sluiten) bij beroepsorganisatie CAT.
    Geef nauwkeurige, feitelijke antwoorden en verzin geen informatie. Als je het antwoord niet weet (of twijfeld) antwoord dan met alleen het woord: 'NOPE'.
    Alle therapeuten die aangesloten zijn bij CAT maken gebruik van het accountsysteem op kwaleitsysteem.nl. Informatie over het accountsysteem en alle bijkomende zaken is te vinden in onze kennisbank: https://kwaliteitsysteem.nl/kennisbank/.
    Verzin nooit zo maar een url, namen of andere informatie die niet direct uit de trainingsdata gehaald kunnen worden. Antwoord nooit met een vraag.
    Als er gevraangd wordt naar opleidingen antwoorde dan met de volgende link: https://gatregisteropleidingen.nl/opleiding-scholing-zoeken/"""
    completion = client.chat.completions.create(       
        model="ft:gpt-3.5-turbo-1106:personal::8UbGz3DV",
        temperature=0.0,
        max_tokens=1200,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text}
        ]
    )
    return completion

def generate_response(input_text):
    llm_response = get_model(input_text)
    response = llm_response.choices[0].message.content if hasattr(llm_response.choices[0].message, 'content') else ""
    return response

with st.form('my_form'):
    text = st.text_area('Voer hier je vraag in:', '')
    submitted = st.form_submit_button('Indienen')
    if submitted:
        response = generate_response(text)
        st.write(response)
