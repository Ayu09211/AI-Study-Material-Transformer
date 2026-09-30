import streamlit as st
from pypdf import PdfReader

from prompts import create_prompt
from ai_service import generate_ai_response

from database import (
    create_database,
    save_result,
    get_history,
    delete_history
)


# ==================================================
# INITIALIZE DATABASE
# ==================================================

create_database()


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Study Material Transformer",
    page_icon="📚",
    layout="wide"
)


# ==================================================
# CUSTOM UI STYLE
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("📚 AI Study Material Transformer")

    page = st.radio(
        "Navigate",
        [
            "🏠 Transform Material",
            "📖 History"
        ]
    )

    st.divider()


# ==================================================
# TRANSFORM MATERIAL PAGE
# ==================================================

if page == "🏠 Transform Material":

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------

    st.markdown(
        '<div class="main-title">'
        '📚 AI Study Material Transformer'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Transform your study material into summaries, notes, '
        'MCQs, flashcards and more using Generative AI.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------
    # TRANSFORMATION SETTINGS
    # --------------------------------------------------

    with st.sidebar:

        st.header("⚙️ Transformation Settings")

        option = st.selectbox(
            "What do you want to generate?",
            [
                "Summary",
                "Study Notes",
                "MCQs",
                "Flashcards",
                "Important Questions",
                "Viva Questions"
            ]
        )


        if option in [
            "MCQs",
            "Flashcards",
            "Important Questions",
            "Viva Questions"
        ]:

            difficulty = st.selectbox(
                "Difficulty Level",
                [
                    "Easy",
                    "Medium",
                    "Hard"
                ]
            )

            question_count = st.selectbox(
                "Number of Questions / Cards",
                [
                    5,
                    10,
                    15,
                    20
                ]
            )

        else:

            difficulty = "Medium"
            question_count = 10


        st.divider()

        st.info(
            "💡 Tip: Upload a clear, text-based PDF "
            "for better AI results."
        )


    # --------------------------------------------------
    # PDF UPLOAD
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '📄 Upload Study Material'
        '</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Choose your study material PDF",
        type=["pdf"]
    )


    # --------------------------------------------------
    # IF PDF IS UPLOADED
    # --------------------------------------------------

    if uploaded_file is not None:

        # Read PDF

        reader = PdfReader(uploaded_file)

        text = ""

        for page_content in reader.pages:

            text += page_content.extract_text() or ""


        # --------------------------------------------------
        # CHECK PDF TEXT
        # --------------------------------------------------

        if not text.strip():

            st.error(
                "❌ No readable text was found in this PDF. "
                "Please upload a text-based PDF."
            )


        else:

            # --------------------------------------------------
            # FILE INFORMATION
            # --------------------------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.success(
                    f"✅ {uploaded_file.name} uploaded successfully!"
                )

            with col2:

                st.metric(
                    "📄 Number of Pages",
                    len(reader.pages)
                )


            # --------------------------------------------------
            # TEXT PREVIEW
            # --------------------------------------------------

            with st.expander(
                "👀 Preview Extracted Study Material"
            ):

                st.text_area(
                    "Extracted Text",
                    text,
                    height=250
                )


            st.divider()


            # --------------------------------------------------
            # GENERATION SECTION
            # --------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '✨ Generate Material'
                '</div>',
                unsafe_allow_html=True
            )

            st.write(
                f"Selected transformation: **{option}**"
            )


            if option in [
                "MCQs",
                "Flashcards",
                "Important Questions",
                "Viva Questions"
            ]:

                st.write(
                    f"Difficulty: **{difficulty}**  |  "
                    f"Count: **{question_count}**"
                )


            # --------------------------------------------------
            # GENERATE BUTTON
            # --------------------------------------------------

            if st.button(
                "✨ Generate",
                type="primary",
                use_container_width=True
            ):

                # Create prompt

                prompt = create_prompt(
                    option,
                    text,
                    difficulty,
                    question_count
                )


                try:

                    # --------------------------------------------------
                    # AI GENERATION
                    # --------------------------------------------------

                    with st.spinner(
                        "🤖 AI is generating your study material..."
                    ):

                        result = generate_ai_response(
                            prompt
                        )


                    # --------------------------------------------------
                    # SAVE TO DATABASE
                    # --------------------------------------------------

                    save_result(
                        uploaded_file.name,
                        option,
                        difficulty,
                        question_count,
                        result
                    )


                    # --------------------------------------------------
                    # SHOW SUCCESS
                    # --------------------------------------------------

                    st.success(
                        "✅ Generation completed and saved to history!"
                    )


                    # --------------------------------------------------
                    # SHOW RESULT
                    # --------------------------------------------------

                    st.subheader(
                        "📖 AI Generated Result"
                    )

                    st.markdown(result)


                    # --------------------------------------------------
                    # DOWNLOAD RESULT
                    # --------------------------------------------------

                    st.download_button(
                        label="📥 Download Result",
                        data=result,
                        file_name=(
                            f"{option.lower().replace(' ', '_')}.txt"
                        ),
                        mime="text/plain",
                        use_container_width=True
                    )


                # --------------------------------------------------
                # ERROR HANDLING
                # --------------------------------------------------

                except Exception as e:

                    error_message = str(e)


                    # Gemini rate limit

                    if (
                        "429" in error_message
                        or "Rate limit" in error_message
                    ):

                        st.warning(
                            "⚠️ Gemini API daily limit has been "
                            "reached. Please try again after "
                            "the quota resets."
                        )


                    else:

                        st.error(
                            "❌ Something went wrong while "
                            "generating the result."
                        )

                        st.caption(
                            "Please check your API configuration "
                            "and try again."
                        )


    else:

        st.info(
            "👆 Upload a PDF above to start transforming "
            "your study material."
        )


# ==================================================
# HISTORY PAGE
# ==================================================

elif page == "📖 History":

    st.title("📖 Generation History")

    st.write(
        "View and manage your previously generated "
        "study materials."
    )

    st.divider()


    # --------------------------------------------------
    # GET HISTORY
    # --------------------------------------------------

    history = get_history()


    # --------------------------------------------------
    # NO HISTORY
    # --------------------------------------------------

    if not history:

        st.info(
            "📭 No generated materials found yet."
        )

        st.write(
            "Generate a study material from the "
            "'Transform Material' page and it will "
            "appear here."
        )


    # --------------------------------------------------
    # DISPLAY HISTORY
    # --------------------------------------------------

    else:

        st.success(
            f"📚 Total saved materials: {len(history)}"
        )


        for record in history:

            record_id = record[0]

            file_name = record[1]

            transformation = record[2]

            difficulty = record[3]

            question_count = record[4]

            result = record[5]

            created_at = record[6]


            # --------------------------------------------------
            # HISTORY CARD
            # --------------------------------------------------

            with st.expander(
                f"📄 {transformation} — {file_name}"
            ):

                st.write(
                    f"🕒 **Created:** {created_at}"
                )

                st.write(
                    f"🎯 **Difficulty:** {difficulty}"
                )

                st.write(
                    f"🔢 **Count:** {question_count}"
                )

                st.divider()


                # --------------------------------------------------
                # RESULT
                # --------------------------------------------------

                st.markdown(result)


                st.divider()


                # --------------------------------------------------
                # DOWNLOAD + DELETE
                # --------------------------------------------------

                col1, col2 = st.columns(2)


                with col1:

                    st.download_button(
                        "📥 Download",
                        data=result,
                        file_name=(
                            f"{transformation.lower().replace(' ', '_')}_"
                            f"{record_id}.txt"
                        ),
                        mime="text/plain",
                        key=f"download_{record_id}",
                        use_container_width=True
                    )


                with col2:

                    if st.button(
                        "🗑️ Delete",
                        key=f"delete_{record_id}",
                        use_container_width=True
                    ):

                        delete_history(
                            record_id
                        )

                        st.success(
                            "Deleted successfully!"
                        )

                        st.rerun()