# 🕵️‍♂️ Plagiarism Detection Engine

This project is a C++-based plagiarism detection tool designed to identify similar code submissions using efficient algorithms like **tokenization**, **hashing**, **winnowing (fingerprinting)**, and **Jaccard similarity**.

---

## 🚀 Features

- 📁 Detect plagiarism across entire folders of code submissions
- 🧠 Uses **n-gram hashing** and **winnowing** for efficient fingerprint generation
- 📊 Calculates **Jaccard similarity** between pairs of submissions
- 👨‍🎓 Supports filtering by problems and users

---

## 🛠️ How It Works

1. **Preprocessing**
   - Removes both single-line (`//`) and multi-line (`/* ... */`) comments
   - Trims trailing whitespaces
   - Tokenizes the source code

2. **Tokenization & Hashing**
   - Splits code into **n-grams** (default `n=3`)
   - Applies **polynomial rolling hash**:
     ```
     hash = Σ (char[i] - '!') × PRIME^i
     ```

3. **Winnowing (Fingerprinting)**
   - Slides a window of size `WINDOW_SIZE` (default 5)
   - Selects the **minimum hash** from each window as a stable fingerprint

4. **Similarity Comparison**
   - Computes **Jaccard similarity**:
     ```
     Jaccard(A, B) = |A ∩ B| / |A ∪ B|
     ```
   - Compares fingerprints of code pairs to detect similarity
---


