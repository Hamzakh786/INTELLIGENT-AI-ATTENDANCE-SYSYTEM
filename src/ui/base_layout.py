import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2rem !important;
                border: 1px solid rgba(26, 31, 61, 0.12);
                border-radius: 3.5rem !important;
            }

            .stApp div[data-testid="stColumn"] [data-testid="stVerticalBlock"] {
                align-items: center;
                text-align: center;
            }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }

            .stApp .block-container {
                max-width: 960px;
                padding: 1.5rem 1.5rem 2rem;
            }
        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            :root {
                --snap-blue: #5865F2;
                --snap-pink: #EB459E;
                --snap-lavender: #E0E3FF;
                --snap-ink: #171923;
                --snap-muted: #687087;
                --snap-field: #F4F6FA;
            }

            /* Hide Streamlit chrome */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            html, body, .stApp {
                font-family: 'Outfit', sans-serif;
                color: var(--snap-ink);
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(2.1rem, 5vw, 3.5rem) !important;
                line-height: 1.1 !important;
                margin-bottom: 0 !important;
                color: var(--snap-ink);
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 1 !important;
                margin-bottom: 0 !important;
                color: var(--snap-ink);
            }

            h3, h4, p, label, [data-testid="stCaptionContainer"] {
                font-family: 'Outfit', sans-serif !important;
            }

            [data-testid="stTextInput"] input,
            [data-testid="stNumberInput"] input,
            [data-testid="stTextArea"] textarea,
            [data-testid="stSelectbox"] [role="combobox"],
            [data-testid="stMultiSelect"] [role="combobox"] {
                background: var(--snap-field) !important;
                border: 1px solid rgba(35, 43, 74, 0.08) !important;
                border-radius: 10px !important;
                color: var(--snap-ink) !important;
                -webkit-text-fill-color: var(--snap-ink) !important;
                caret-color: var(--snap-blue);
                min-height: 2.65rem;
            }

            [data-testid="stTextInput"] input::placeholder,
            [data-testid="stNumberInput"] input::placeholder,
            [data-testid="stTextArea"] textarea::placeholder {
                color: var(--snap-muted) !important;
                -webkit-text-fill-color: var(--snap-muted) !important;
                opacity: 1;
            }

            [data-testid="stWidgetLabel"],
            [data-testid="stWidgetLabel"] p {
                color: var(--snap-ink) !important;
            }

            [data-testid="stRadio"] [role="radiogroup"] {
                gap: 0.65rem;
            }

            [data-testid="stRadio"] label {
                background: rgba(255, 255, 255, 0.62);
                border: 1px solid rgba(35, 43, 74, 0.1);
                border-radius: 999px;
                padding: 0.35rem 0.9rem;
            }

            [data-testid="stButton"] > button[kind="primary"],
            [data-testid="stButton"] > button[kind="secondary"],
            [data-testid="stButton"] > button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 0.65rem 1.15rem !important;
                border: 0 !important;
                transition: transform 0.18s ease, filter 0.18s ease !important;
            }

            [data-testid="stButton"] > button[kind="primary"] {
                background-color: var(--snap-blue) !important;
            }

            [data-testid="stButton"] > button[kind="secondary"] {
                background-color: var(--snap-pink) !important;
            }

            [data-testid="stButton"] > button[kind="tertiary"] {
                background-color: var(--snap-ink) !important;
            }

            [data-testid="stButton"] > button[kind="primary"]:hover,
            [data-testid="stButton"] > button[kind="secondary"]:hover,
            [data-testid="stButton"] > button[kind="tertiary"]:hover {
                transform: translateY(-1px);
                filter: brightness(1.05);
            }

            [data-testid="stAlert"] {
                border-radius: 10px;
            }

            [data-testid="stDataFrame"] {
                border: 1px solid rgba(35, 43, 74, 0.12);
                border-radius: 12px;
                overflow: hidden;
            }

            [data-testid="stCameraInput"], [data-testid="stAudioInput"] {
                border-radius: 12px;
                overflow: hidden;
            }

            @media (max-width: 640px) {
                .stApp .block-container {
                    padding: 1rem 1rem 1.5rem;
                }

                h2 {
                    font-size: 1.45rem !important;
                }
            }
        </style>  

                """
            ,unsafe_allow_html=True)