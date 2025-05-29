# Completion Meter using Collector Curve & Clustering

This project explores how we can **track the "completion" of a conversation or speech** using a graph called a **collector curve**. The goal is to eventually detect when a speaker is likely to finish speaking or when is topic going to end using patterns in **entities**, **noun phrases**, and their repetitions.

---

## ✅ What is Completed So Far

- Collect 25 speeches and 25 conversations
- **Extracted entities and noun phrases** from sample speeches
- **Generated collector curves** that track how many *new* concepts appear over time
- Chunked each speech into small segments
- Generated **vector embeddings** for each chunk using sentence-transformers
- Clustered similar chunks using unsupervised learning (KMeans)
- Added a synthetic **progress** label to each chunk to show "how far" into speech it is
- Trained a **Random Forest Regressor** to predict **progress** from embeddings (supervised learning)

```
NOTE: This baseline model is just a starting point, accuracy is limited due to repetitive/generic data but the main goal was to prepare pipeline which is complete and modular - easy to re-run with better speech datasets
```

---

## 📁 Project Structure

| File/Folder | Purpose |
|-------------|---------|
| `/data` | GPT generated data in `.txt` format |
| `/data_tedex_speeches/ted_talks.json` | Ted speeches in `.json` format |
| `/data_tedex_speeches/csv_to_json.ipynb` | Script to convert `.csv` from kaggle into `.json` |
| `/spacy/script.py` | Script to separate noun_phrases from `/data` and add it to `/extracted_data.json`|
| `/spacy/script_tedex.py` | Script to separate noun_phrases from tedEx data and add it to `/extracted_data_tedex.json` |
| `/extracted_data_cleaned.json` | Cleaned file of extracted `entities` and `noun_phrases` per speech |
| `/extracted_data_tedex_3.json` | Extracted `entities` and `noun_phrases` per tedEx data |
| `/curve/curve_analysis.ipynb` | Script to generate collector graphs |
| `/curve/curve_analysis_tedex.ipynb` | Script to generate collector graphs for tedex data |
| `/curve/graphs_collector_style` | Collector curve graphs for each speech => generate it for yourself using `/curve/curve_analysis.ipynb` |
| `/curve/graph_collector_style_tedex` | Collector curve graphs for each tedex speech => generate it for yourself using `/curve/curve_analysis_tedex.ipynb` |
| `/clustering/generate_chunk.ipynb` | Script to chunk `/data` files and store in `/chunked_data` |
| `/clustering/generate_chunk_tedex.ipynb` | Script to chunk `/extracted_data_tedex_3.json` and store it in `/chunked_data_tedex` |
| `/chunked_data` | Speech chunks stored as JSON after splitting to generate vector embeddings => generate it for yourself using `/clustering/cluster_chunks.ipynb` |
| `/chunked_data_tedex` | Chunks for ted talks => generate it for yourself using => `/clustering/generate_chunk_tedex.ipynb` |
| `/clustering/embed_chunks.ipynb` | Script to embed `/chunked_data` using sentence-transformers into `/clustering/chunk_embeddings.json`|
| `/clustering/chunk_embeddings.json` | Chunk embeddings used for generating clusters |
| `/clustering/cluster_chunks.ipynb` | Script to cluster `/clustering/chunk_embeddings.json` and save to `/clustering/chunk_clusters.json`|
| `/clustering/chunk_clusters.json` | Chunks with assigned cluster labels |
| `/clustering/add_progress_labels.ipynb` | Script to add `progress` field (0 to 1) based on chunk order in speech and save to `/clustering/chunk_clusters_labeled.json` |
| `/clustering/chunk_clusters_labeled.json` | Final dataset with `embedding`, `cluster` and `progress` |
| `/clustering/train_regressor.ipynb` | Trains regression model to predict `progress` from chunk embeddings |


---

## Next Steps

1. **Collect Real Conversations**  
   - Collect transcripts of podcasts, debates, interviews, phone calls
   - More diverse and natural speech patterns will improve model training
   - Planned speeches can be used for regression while unplanned ones like stand up comedy or podcasts can be used for curve shape analysis

2. **Better Embeddings & Curve Analysis**
   - Need to experiment with advanced embeddings like BERT variants
   - Deflect **flattening regions** of collector curve to identify conversation nearning completion

3. **Work on third approach**
   - Collect speeches and take out keywords
   - Associate keywords with subtopics
   - Make proper algorithm to calculate conversation percentage completed

---