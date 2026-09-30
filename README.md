# 📚 AI Study Material Transformer

An AI-powered academic assistant that transforms study material into useful and exam-oriented learning resources using Generative AI.

---

## 📌 Project Overview

The **AI Study Material Transformer** is a Generative AI-based application designed to help students convert their study material into different learning formats.

Users can upload a PDF containing study material and generate:

- 📄 Summaries
- 📝 Study Notes
- ❓ Multiple Choice Questions (MCQs)
- 🧠 Flashcards
- 📚 Important Examination Questions
- 🎤 Viva Questions

The application uses structured prompt engineering to generate relevant and easy-to-understand educational content.

---

## 🎯 Objectives

The main objectives of the project are:

1. To simplify lengthy study material using Generative AI.
2. To provide exam-oriented study resources.
3. To generate different types of learning content from the same source material.
4. To demonstrate the practical use of Prompt Engineering.
5. To provide an easy-to-use interface for students.
6. To store previously generated materials for future reference.

---

## ✨ Key Features

### 📄 PDF Upload

Users can upload text-based PDF study materials.

### 🤖 AI Content Generation

The application uses Google's Gemini Generative AI model to transform the uploaded content.

### 📝 Multiple Learning Formats

Users can generate:

- Summary
- Study Notes
- MCQs
- Flashcards
- Important Questions
- Viva Questions

### 🎯 Difficulty Selection

For question-based outputs, users can select:

- Easy
- Medium
- Hard

### 🔢 Custom Question Count

Users can choose the number of questions or flashcards:

- 5
- 10
- 15
- 20

### 📥 Download Generated Content

Generated results can be downloaded as text files.

### 💾 Generation History

The application stores previously generated materials using SQLite.

Users can:

- View previous results
- Download previous results
- Delete previous results

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Streamlit | User interface |
| Google Gemini API | Generative AI |
| Prompt Engineering | AI content generation |
| PyPDF | PDF text extraction |
| SQLite | Database and history |
| python-dotenv | Secure API key management |

---

## 🏗️ System Architecture

```text
              AI STUDY MATERIAL TRANSFORMER
                         │
                         ▼
                ┌─────────────────┐
                │    Streamlit    │
                │    Frontend     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    PDF Upload   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  PDF Extraction │
                │     PyPDF       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Prompt Engine   │
                │  prompts.py     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Gemini AI     │
                │   AI Service    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Generated Study │
                │    Material     │
                └────────┬────────┘
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          Display     Download    SQLite
                                  History