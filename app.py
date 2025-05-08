import os
import pandas as pd
import streamlit as st
import tempfile
import time

# Load the dataset
excel_file_path = "ISL_CSLRT_Corpus/ISL_CSLRT_Corpus details.xlsx"

try:
    sheets = pd.read_excel(excel_file_path, sheet_name=None)  # Load all sheets
    english_df = sheets[list(sheets.keys())[0]]  # First sheet (English)
    tamil_df = sheets[list(sheets.keys())[1]]  # Second sheet (Tamil)

    # Strip column names of extra spaces
    english_df.columns = english_df.columns.str.strip()
    tamil_df.columns = tamil_df.columns.str.strip()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    english_df, tamil_df = None, None

# Function to ensure the video path follows strict format
def is_valid_path(video_path):
    return video_path.startswith("Videos_Sentence_Level/") or video_path.startswith("Videos_Sentence_Level\\")

# Function to fetch video path from dataset
def get_video_from_dataset(query, language):
    df = english_df if language == "English" else tamil_df
    if df is not None:
        matching_video = df[df['Sentences'].str.strip().str.lower() == query.strip().lower()]
        if not matching_video.empty:
            video_path = matching_video.iloc[0]['File location'].strip().replace("\\", "/")
            if not is_valid_path(video_path):
                st.error("Invalid video path format in Excel. Must be inside 'Videos_Sentence_Level/'.")
                return None
            video_full_path = os.path.join("ISL_CSLRT_Corpus", video_path)
            if os.path.exists(video_full_path):
                return video_full_path
            else:
                st.error(f"Video not found at {video_full_path}")
                return None
    return None

# Function to fetch text from uploaded video filename
def get_text_from_uploaded_video(uploaded_filename, language):
    df = english_df if language == "English" else tamil_df
    if df is not None:
        for idx, row in df.iterrows():
            video_path = row['File location']
            if isinstance(video_path, str) and is_valid_path(video_path):
                filename = os.path.basename(video_path).strip().lower()
                if uploaded_filename.strip().lower() == filename:
                    return row["Sentences"]
    st.error(f"No matching text found for video `{uploaded_filename}` or invalid path format.")
    return None

# Streamlit UI
language_option = st.selectbox("Select Language", ["English", "தமிழ்"])

if language_option == "English":
    st.title("BI-Directional Sign Language Translation System")
    text_input_label = "Enter Text to get the corresponding Sign Language Video:"
    search_button_label = "Search Video"
else:
    st.title("இரு திசை சைகை மொழி மொழிபெயர்ப்பு அமைப்பு")
    text_input_label = "செயல் மொழியின் காணொளியை பெற உரையை உள்ளிடவும்:"
    search_button_label = "காணொளியை தேடவும்"

# Tabs for functionalities
tab1, tab2 = st.tabs(["Text to Sign Video", "Sign Video to Text"])

# Session state for Tamil input
if "tamil_input" not in st.session_state:
    st.session_state.tamil_input = ""

# --- TAB 1: Text to Sign Video Conversion ---
with tab1:
    if language_option == "English":
        query = st.text_input(text_input_label)
    else:
        st.subheader("தமிழ் விசைப்பலகை (Tamil Keyboard)")
        tamil_keyboard_layout = [
            ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"],
            ["க", "ங", "ச", "ஞ", "ட", "ண", "த", "ந", "ப", "ம"],
            ["ய", "ர", "ல", "வ", "ழ", "ள", "ற", "ன"],
            ["ா", "ி", "ீ", "ு", "ூ", "ெ", "ே", "ை", "ொ", "ோ", "ௌ", "்"]
        ]
        for row in tamil_keyboard_layout:
            cols = st.columns(len(row))
            for index, letter in enumerate(row):
                if cols[index].button(letter, key=f"tamil_{letter}"):
                    st.session_state.tamil_input += letter
        query = st.text_input(text_input_label, st.session_state.tamil_input, key="tamil_text_input")

    if st.button(search_button_label):
        video_path = get_video_from_dataset(query, language_option)
        if video_path:
            st.video(video_path)
        else:
            st.warning("No video found for the given text.")

# --- TAB 2: Sign Video to Text Conversion ---
with tab2:
    uploaded_file = st.file_uploader("Upload a sign language video to get the corresponding text", type=["mp4"])

    if uploaded_file is not None:
        uploaded_filename = uploaded_file.name
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_video_path = temp_file.name

        with st.spinner('Processing... Please wait'):
            time.sleep(3)
            st.video(temp_video_path)

            detected_text = get_text_from_uploaded_video(uploaded_filename, language_option)
            if detected_text:
                st.success(f"Detected Text from Video: **{detected_text}**")
            else:
                st.warning("No matching text found for this video in the dataset.")
