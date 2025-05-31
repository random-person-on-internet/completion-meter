# Completion Meter using Collector Curve & Clustering

This project explores how we can **track the "completion" of a conversation or speech** using a graph called a **collector curve**. The idea is to measure how many new concepts are introduced over time and predict how far along a speaker is in their discourse.

> I attempted multiple approaches using real and synthetic data, exploring both unsupervised clustering and supervised regression. While the results were not ideal, the pipeline is now complete and modular—ready to support more advanced strategies.

---

## ✅ What is Completed So Far

- Collect 25 AI-generated speeches and 25 conversations
- **Extracted entities and noun phrases** using spaCy
- **Generated collector curves** that track how many *new* concepts appear over time
- Chunked each speech into small segments
- Generated **vector embeddings** for each chunk using sentence-transformers
- Clustered similar chunks using unsupervised learning (KMeans)
- Added a synthetic **progress** label to each chunk to show "how far" into speech it is (0 = start, 1 = end)
- Trained a **Random Forest Regressor** to predict **progress** from embeddings (supervised learning)

**Result:** Despite over 90,000 training samples, model performance was limited (MSE ~ 0.2). This confirms that these methods alone aren't sufficient to predict speech completion reliably

---

## 📁 Project Structure

| File/Folder | Purpose |
|-------------|---------|
| `/data/data_AI_generated` | AI generated speeches (25) and conversations (25)|
| `/data/data_tedex_speeches` | Original TEDx speeches + CSV-to-JSON conversion notebook |
| `/spacy` | Scripts to extract `noun_phrases` and `entities` from data|
| `/curve` | Scripts and output for generating collector curves |
| `/clustering/scripts` | Main pipeline for chunking, embedding, clustering and regression |
| `/clustering/models` | Trained regression models |
| `/clustering/chunked_data`, `/embeddings`, `/clusters`, `/labelled` | Intermediate clustering data |
| `/ignore` | Temporary files and unused experiments |
| `.gitignore` | Filters out all large generated files for clean GitHub repo, you can check it here to structure your folder structure accordingly |

---

## ⚙️ Technical Pipeline

The project follows a modular structure:

```
1. Text Collection  ➝  /data or /data_tedex_speeches
2. Entity/Noun Phrase Extraction  ➝  /spacy/
3. Collector Curve Visualization  ➝  /curve/
4. Speech Chunking  ➝  /clustering/scripts/generate_chunks.ipynb
5. Embedding Generation  ➝  /clustering/scripts/embed_chunks.ipynb
6. Clustering Chunks  ➝  /clustering/scripts/cluster_chunks.ipynb
7. Labeling with Progress %  ➝  /clustering/scripts/add_progress_label.ipynb
8. Regression Training  ➝  /clustering/scripts/train_regressor.ipynb / train_reg.py
```

All intermediate files (chunks, embeddings, clusters, graphs) can be re-generated using the notebooks.

---

## 📉 Results

After testing with both synthetic and real TEDx speech data (3995+ speeches), the regression model's MSE score hovered around **0.2**, indicating low predictive power.

* **Mean Absolute Error**: \~0.21
* **R² Score**: \~0.11
* **Explained Variance**: \~0.11

**Lesson Learned**: Predicting speech completion from embeddings and synthetic progress labels isn't robust—especially when content is repetitive or generic.

---

## What’s Next

Now shifting to a more **semantic and topic-aware** method:

1. **Subtopic Extraction**

   * Extract core keywords or concepts for each speech
   * Cluster them into meaningful **subtopics**
   * Link each chunk of speech to a subtopic

2. **Progress Estimation Using Subtopics**

   * Track which subtopics have been covered and in what order
   * Use topic coverage and density to estimate percentage completion

This approach focuses on **semantic progression**, not just surface-level lexical change.

---

## Thoughts on project so far

While the "completion prediction" didn't work as expected, the pipeline is solid and the next stage has a much clearer direction.

---