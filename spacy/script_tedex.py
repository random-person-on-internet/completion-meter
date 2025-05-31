import spacy
import json
from pathlib import Path

# from collections import Counter

nlp = spacy.load("en_core_web_sm")


def extract_info(text):
    doc = nlp(text)
    entities = list(
        set(
            [
                ent.text
                for ent in doc.ents
                if ent.label_ not in ["DATE", "TIME", "PERCENT", "MONEY", "QUANTITY"]
            ]
        )
    )
    # noun_phrases = list(set([chunk.text for chunk in doc.noun_chunks]))
    noun_phrases = []
    for chunk in doc.noun_chunks:
        #     filtered_tokens = [
        #         token.lemma_.lower()
        #         for token in chunk
        #         if not token.pos_ in ["NOUN", "PROPN"]
        #     ]
        #     if filtered_tokens:
        #         normalized = " ".join(filtered_tokens)
        #         noun_phrases.append(normalized)
        # noun_phrases = list(set(noun_phrases))

        tokens = [token for token in chunk if token.pos_ == "NOUN"]
        lemmas = [token.lemma_.lower() for token in tokens]
        if lemmas:
            phrase = " ".join(lemmas)
            noun_phrases.append(phrase)

    return entities, noun_phrases


def process_json(input_json_path):
    print(f"📄 Loading from: {input_json_path.resolve()}")

    with open(input_json_path, "r", encoding="utf-8") as f:
        ted_data = json.load(f)

    extracted = {}

    i = 0

    for item in ted_data:
        talk_id = item.get("talk_id", "unknown_id")
        title = item.get("title", "Untitled").strip()
        transcript = item.get("transcript", "").strip()

        if not transcript or len(transcript.split()) < 50:
            print(f"⏭️ Skipping talk ID {talk_id} (too short or empty)")
            continue

        print(f"Value of i: {i}")
        print(f"{i*100/3995:.4f}% done")
        i += 1

        print(f"🔍 Processing: {title[:40]}...")

        entities, noun_phrases = extract_info(transcript)
        print(f"📌 Found {len(entities)} entities and {len(noun_phrases)} noun phrases")

        extracted[talk_id] = {
            "title": title,
            "entities": entities,
            "noun_phrases": noun_phrases,
        }

    with open(
        "/curve/extracted_data/extracted_data_tedex_3.json", "w", encoding="utf-8"
    ) as f:
        json.dump(extracted, f, indent=2, ensure_ascii=False)

    print("✅ Extraction complete. Data saved to extracted_data_tedex.json")


if __name__ == "__main__":
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[1]

    input_path = project_root / "/data/data_tedex_speeches/ted_talks.json"
    process_json(input_path)
