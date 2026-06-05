import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="AI Translator Pro",
    page_icon="🌍",
    layout="centered"
)

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>

body {
    background-color: #f5fbff;
}

h1 {
    color: #1e88e5;
    text-align: center;
}

.stButton > button {
    background-color: #1e88e5;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background-color: #1565c0;
}

section[data-testid="stSidebar"] {
    background-color: #e3f2fd;
}

.result-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #e8f5e9;
    color: black;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown("""
# 🌍 AI-Powered Language Translator

### Translate text instantly using Artificial Intelligence

---
""")

# ==========================
# LANGUAGES
# ==========================
languages = {
    "🌐 Auto Detect": "auto",
    "🇬🇧 English": "en",
    "🇮🇳 Hindi": "hi",
    "🇮🇳 Marathi": "mr",
    "🇪🇸 Spanish": "es",
    "🇫🇷 French": "fr",
    "🇩🇪 German": "de",
    "🇯🇵 Japanese": "ja",
    "🇨🇳 Chinese": "zh-CN",
    "🇸🇦 Arabic": "ar",
    "🇷🇺 Russian": "ru",
    "🇮🇹 Italian": "it",
    "🇰🇷 Korean": "ko",
    "🇵🇹 Portuguese": "pt"
}

# ==========================
# TRANSLATION HISTORY
# ==========================
if "history" not in st.session_state:
    st.session_state.history = []

# ==========================
# SIDEBAR
# ==========================
st.sidebar.header("⚙ Settings")

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys())
    )

# ==========================
# INPUT TEXT
# ==========================
text = st.text_area(
    "✍ Enter text to translate",
    height=150
)

# Character Counter
st.caption(f"Characters: {len(text)}")

# ==========================
# TRANSLATE BUTTON
# ==========================
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

        st.markdown("### 📌 Translation Result")

        st.markdown(
            f"""
            <div class="result-box">
            {translated}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Save history
        st.session_state.history.append(
            f"{source_language} ➜ {target_language}: {translated}"
        )

        # Copy Area
        st.text_area(
            "📋 Copy Translation",
            translated,
            height=120
        )

        # ==========================
        # TEXT TO SPEECH
        # ==========================
        try:
            tts = gTTS(text=translated)
            tts.save("translation.mp3")

            audio_file = open("translation.mp3", "rb")

            st.markdown("### 🔊 Listen to Translation")

            st.audio(audio_file.read())

        except:
            st.warning("Audio generation not available.")

# ==========================
# HISTORY
# ==========================
st.sidebar.markdown("---")
st.sidebar.subheader("📜 Translation History")

for item in reversed(st.session_state.history):
    st.sidebar.write(item)