import streamlit as st
from deep_translator import GoogleTranslator

# Page configuration
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="centered"
)


# ===== CUSTOM CSS (Light Blue Theme) =====
st.markdown("""
<style>

body {
    background-color: #f5fbff;
}

/* Main title */
h1 {
    color: #1e88e5;
    text-align: center;
}

/* Subtitle */
p {
    text-align: center;
    color: #555;
}

/* Text area */
textarea {
    border-radius: 10px !important;
    border: 2px solid #90caf9 !important;
}

/* Buttons */
.stButton > button {
    background-color: #1e88e5;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #1565c0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #e3f2fd;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 AI Language Translator")
st.write("Translate text instantly using AI")

# Language dictionary
languages = {    "Auto Detect": "auto",

    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

# Sidebar (Professional UI style)
st.sidebar.header("⚙ Settings")

source_language = st.sidebar.selectbox(
    "Source Language",
    list(languages.keys())
)

target_language = st.sidebar.selectbox(
    "Target Language",
    list(languages.keys())
)

# Swap button
if st.sidebar.button("🔄 Swap Languages"):
    source_language, target_language = target_language, source_language

# Input box
text = st.text_area("✍ Enter text to translate")

# Translate button
if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter text first!")
    else:
        with st.spinner("Translating..."):

            translated = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(text)

           

        st.success("✅ Translation Complete")
        st.markdown("### 📌 Result")
        st.info(translated)

        # Copy feature
        st.code(translated)