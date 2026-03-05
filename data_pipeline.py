# Multilingual Nigeria NLU - Initial Data Curation Pipeline
# Author: Umar Yusuf Lamiya

dataset = {
    "hausa": [
        {"input": "Ina kwana", "label": "morning_greeting", "en": "Good morning"},
        {"input": "Ina son ganin likita", "label": "medical_request", "en": "I want to see a doctor"},
        {"input": "Ina ne babban kanti?", "label": "location_query", "en": "Where is the big shop?"}
    ],
    "fulfulde": [
        {"input": "Jam waali", "label": "morning_greeting", "en": "Good morning"},
        {"input": "Mido yidi yi'ugo lokotoro", "label": "medical_request", "en": "I want to see a doctor"}
    ]
}

def preprocess_text(text):
    # Basic normalization for Nigerian indigenous languages
    return text.lower().strip()

print(f"Dataset initialized with {len(dataset['hausa'])} Hausa and {len(dataset['fulfulde'])} Fulfulde entries.")
