import spacy
from pathlib import Path
import json

# spacy English model
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
    noun_phrases = list(set([chunk.text for chunk in doc.noun_chunks]))
    return entities, noun_phrases


def process_folder(folder_path):
    folder = Path(folder_path)
    print("📁 Absolute folder path:", folder.resolve())
    all_data = {}

    txt_files = list(folder.glob("*.txt"))
    print(f"📄 Found {len(txt_files)} .txt files")

    for file in txt_files:
        print(f"🔍 Processing: {file.name}")
        text = file.read_text(encoding="utf-8")
        entities, noun_phrases = extract_info(text)
        print(f"📌 Found {len(entities)} entities and {len(noun_phrases)} noun phrases")
        all_data[file.name] = {"entities": entities, "noun_phrases": noun_phrases}

    with open("extracted_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    print("✅ Extraction complete. Data saved to extracted_data.json")


if __name__ == "__main__":
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data"

    process_folder(data_path)
