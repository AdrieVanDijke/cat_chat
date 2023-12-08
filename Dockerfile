# Gebruik een officiële Python runtime als ouder image
FROM python:3.11.6

# Stel de werkdirectory in de container in
WORKDIR /app

# Kopieer de huidige directory inhoud in de container bij /app
COPY . /app

# Installeer de benodigde pakketten uit requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Maak poort 8501 beschikbaar voor de wereld buiten deze container
EXPOSE 8501

# Definieer het commando om de applicatie te draaien
CMD ["streamlit", "run", "app.py"]