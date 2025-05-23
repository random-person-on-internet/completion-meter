# Completion Meter using Collector Curve & Clustering

This project explores how we can **track the "completion" of a conversation or speech** using a graph called a **collector curve**. The goal is to eventually detect when a speaker is likely to finish speaking or when is topic going to end using patterns in **entities**, **noun phrases**, and their repetitions.

---

## ✅ What is Completed So Far

- Collect 25 speeches and 25 conversations
- **Extracted entities and noun phrases** from sample speeches
- **Generated collector curves** that track how many *new* concepts appear over time
- These curves help us **visualize novelty vs repetition** in a speech
- The first dataset mostly had **planned speeches**, so the curves appear mostly linear which indicates less repetition

You can find the generated collector curve graphs inside:
```

📁 \curve\curve_analysis.ipynb

```

---

## 📁 Project Structure

| File/Folder | Purpose |
|-------------|---------|
| `\spacy\script.py` | Helps us separate noun_phrases from data and add it to `/extracted_data.json`|
| `\extracted_data_cleaned.json` | Main input file with cleaned extracted `entities` and `noun_phrases` per speech |
| `\curve\graphs_collector_style\` | Auto-generated graphs showing collector curves for each speech |
| `\curve\curve_analysis.ipynb` | Python scripts to generate collector graphs |
| `\data` | Data collected for further steps |


---

## Next Steps

1. **Collect Real Conversations**  
   - We need to gather more **natural dialogues** (eg: phone calls, interviews, podcasts)
   - This will help us compare **collector curves of real vs planned speech**

2. **Clustering & Flattening Detection**  
   - We'll analyze the collector curve shape to detect **flattening** (i.e, when fewer new concepts appear)
   - The idea is: if the curve flattens, the conversation might be **nearing completion**
   - Will experiment with **clustering similar patterns** across different conversations
   - Clustering will help us track progress along with collector graph as it can work for **planned speeches too**

---