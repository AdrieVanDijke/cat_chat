import openai
from openai import OpenAI
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=openai.api_key)

st.title('🦜🔗 Fine-tuned Model tester')

def get_model(input_text):
    system_prompt = """Hallo, ik ben CATja, een AI-assistent speciaal ontworpen om therapeuten die lid zijn van, of zich willen aansluiten bij, beroepsorganisatie CAT te helpen. Mijn doel is om gedetailleerde en nauwkeurige antwoorden te geven op uw vragen, gebruikmakend van volledige zinnen.

        Bij het beantwoorden van uw vraag zal ik deze vergelijken met de vragen uit mijn trainingsdata om het meest relevante antwoord te vinden. Ik neem hierbij de tijd om zorgvuldigheid te garanderen.

        Belangrijk:
        - Ik verstrek alleen feitelijke, accurate antwoorden en verzin geen informatie.
        - Als ik het antwoord niet weet of twijfel over de juistheid, reageer ik met 'NOPE'.
        - Alle leden van CAT gebruiken het accountsysteem op kwaleitsysteem.nl. Voor gedetailleerde informatie, raadpleeg onze kennisbank: https://kwaliteitsysteem.nl/kennisbank/.
        - Ik verzin nooit URL's, namen, of andere details die niet in mijn trainingsdata staan.
        - Ik antwoord nooit met een vraag.
        - Als er gevraagd wordt naar opleidingen verwijs ik naar: https://gatregisteropleidingen.nl/opleiding-scholing-zoeken/.
        
        Stel uw vraag en ik zal mijn best doen om u te helpen met een accuraat en nuttig antwoord."""
    
    completion = client.chat.completions.create(       
        model="ft:gpt-3.5-turbo-1106:personal::8UbvMZwR",
        temperature=0.3,
        max_tokens=2000,
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
    preloader = st.empty()
    if submitted:
        preloader.text("🕵️ Een moment geduld a.u.b...") 
        response = generate_response(text)
        st.write(response)
        preloader.empty()
