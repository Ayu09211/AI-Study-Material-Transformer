def create_prompt(option, text, difficulty, question_count):

    if option == "Summary":
        return f"""
You are an expert academic tutor.

Read the study material given below and create a clear and concise summary.

Requirements:
- Cover the important concepts.
- Keep important technical terms.
- Use simple language.
- Use headings and bullet points.
- Do not add information that is not present in the study material.

Study Material:
{text}
"""

    elif option == "Study Notes":
        return f"""
You are an expert academic tutor helping an undergraduate student prepare for examinations.

Convert the following study material into well-organized study notes.

Requirements:
- Use clear headings and subheadings.
- Explain important concepts in simple language.
- Include important definitions.
- Include formulas if present.
- Highlight important points.
- Make the notes exam-oriented.
- Do not add information that is not present in the study material.

Study Material:
{text}
"""

    elif option == "MCQs":
        return f"""
You are an academic question-paper generator.

Create exactly {question_count} multiple-choice questions from the study material.

Difficulty level: {difficulty}

For every question provide:
1. Question
2. Four options (A, B, C, D)
3. Correct answer
4. Short explanation

Requirements:
- Generate exactly {question_count} questions.
- Questions must be based only on the supplied study material.
- Match the selected difficulty level: {difficulty}.
- Include a mixture of conceptual and factual questions.
- Avoid duplicate questions.
- Number the questions from 1 to {question_count}.

Study Material:
{text}
"""

    elif option == "Flashcards":
        return f"""
You are an academic tutor.

Convert the following study material into useful revision flashcards.

Create exactly {question_count} flashcards.

Difficulty level: {difficulty}

For each flashcard provide:
Front: Question or key concept
Back: Short and accurate answer

Requirements:
- Generate exactly {question_count} flashcards.
- Use simple language.
- Focus on important concepts.
- Match the selected difficulty level.
- Avoid duplicate flashcards.

Study Material:
{text}
"""

    elif option == "Important Questions":
        return f"""
You are an experienced university examination question setter.

Analyze the study material and generate exactly {question_count} important questions that a student should prepare for an examination.

Difficulty level: {difficulty}

Include a suitable mixture of:
- Short-answer questions
- Conceptual questions
- Long-answer questions

For each question, provide a brief indication of what the answer should cover.

Requirements:
- Generate exactly {question_count} questions.
- Match the selected difficulty level.
- Base all questions only on the supplied study material.
- Avoid duplicate questions.

Study Material:
{text}
"""

    elif option == "Viva Questions":
        return f"""
You are an experienced viva examiner.

Generate exactly {question_count} important viva questions from the study material.

Difficulty level: {difficulty}

For each question provide:
- The question
- A short and simple answer

Requirements:
- Generate exactly {question_count} questions.
- Focus on definitions, concepts, applications, and important technical points.
- Match the selected difficulty level.
- Avoid duplicate questions.
- Number the questions from 1 to {question_count}.

Study Material:
{text}
"""

    else:
        return f"""
Read and explain the following study material clearly.

Study Material:
{text}
"""