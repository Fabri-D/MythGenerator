# 🐉 MythGenerator

**MythGenerator** is a domain-specific GPT-2 text generation system fine-tuned to produce original mythological narratives from structured prompts.

The model was trained on a curated dataset of mythological entities across multiple cultures and then deployed as a standalone inference application with a graphical interface.

> ⚠️ All AI-generated content is fictional.

---

## 📌 Project Overview

MythGenerator explores controlled creative text generation through domain-specific fine-tuning.

The development process included:

1. Compilation of **470 mythological entities** across cultures.
2. Automated content retrieval via the **Wikipedia API**.
3. Filtering and cleaning for mythologically relevant material.
4. Reduction to **370 curated articles**.
5. Structured JSON formatting.
6. Conversion into GPT-2–compatible training sequences.
7. Addition of structural dialogue tokens (`USER`, `ASSISTANT`) to simulate conditional prompting.
8. Fine-tuning of GPT-2 on the curated dataset.

The objective was not general storytelling, but stylistically coherent myth-style narrative generation.

---

## 🧠 Model Architecture

- Base model: **GPT-2**
- Framework: **HuggingFace Transformers**
- Backend: **PyTorch**
- Training objective: Autoregressive (causal language modeling)
- Optimization: Token-level cross-entropy
- Conditioning: Structured prompt formatting

The model generates continuations from prompts of the form:

> "In an ancient world, there was a myth of..."

and produces culturally-inspired myth narratives.

---

## 🖥️ Application Interface

The repository includes a runnable graphical interface built in Python.

Features:

- Prompt input field  
- Generate button  
- Text output panel  
- Local inference using the fine-tuned model  

The interface allows real-time generation without requiring retraining.

---

## 🐺 Example — Cave Wolf

Prompt:
> "In an ancient world, there was a myth of a cave wolf"

Generated output:

![Cave Wolf Example](cap01.jpg)

---

## 🦊 Example — Shadow Fox

Prompt:
> "In an ancient world, there was the myth of the Shadow Fox"

Generated output:

![Shadow Fox Example](cap02.jpg)

---

## 🎥 Video Explanation (Spanish)

This repository includes a full explanation video covering:

- Dataset construction  
- Filtering methodology  
- Fine-tuning pipeline  
- Application design  

Watch here:

👉 https://github.com/Fabri-D/MythGenerator/blob/master/MythGeneratorVideo.mp4

---

## 📦 Repository Contents

This repository includes:

- `interfaz.py` — graphical inference interface  
- `model/` — fine-tuned GPT-2 model weights  
- Example output screenshots  
- Video explanation  
- Documentation  

The dataset, preprocessing scripts, and training pipeline used for fine-tuning are **not included** in this repository.

---

## 🧪 Purpose

MythGenerator serves as an experimental demonstration of:

- Domain-specific language model fine-tuning  
- Cultural dataset curation  
- Controlled generative modeling  
- Structured prompt conditioning  
- Creative AI prototyping  

It represents an early exploration of deterministic structure combined with generative language modeling.

---

## ⚠️ Disclaimer

All generated content is fictional and produced by a fine-tuned language model trained on publicly available mythological sources.

This project is intended for research and experimental purposes only.
