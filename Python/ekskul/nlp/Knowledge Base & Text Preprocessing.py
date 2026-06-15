import re

KNOWLEDGE_BASE = {
    "what is taman rama": "Taman Rama is an international school in Bali that provides education from kindergarten to senior high school.",
    "curriculum taman rama": "Taman Rama combines the Indonesian National Curriculum with international programs such as Cambridge Assessment.",
    "facilities taman rama": "The school has libraries, science laboratories, sports fields, music rooms, and computer labs.",
    "extracurricular activities taman rama": "Students can join sports, music, art, dance, and debate clubs."
}

def preprocess_text(text):
    # convert to lowercase
    text = text.lower()
    # remove symbols/numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_response(user_input):
    processed = preprocess_text(user_input)
    if processed in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[processed]
    else:
        return "Sorry, I don't have information about that."

user = "What IS Taman Rama SCHOOL??"
print("User :", user)

response = get_response(user)
print("Bot :", response)
