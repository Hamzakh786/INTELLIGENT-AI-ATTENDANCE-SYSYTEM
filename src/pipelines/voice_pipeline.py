from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np 
import io
import librosa #edt audio processing
import streamlit as st


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        if not audio_bytes:
            raise ValueError('No audio was recorded')

        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        if audio.size == 0:
            raise ValueError('The recording contains no audio')
        if audio.size < sr:
            raise ValueError('Please record at least one second of audio')

        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error(f'Voice recognition failed. Record a clear 1-5 second clip and try again. Details: {e}')
        return None
    

def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0
    
    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding is not None:
            candidate = np.asarray(stored_embedding, dtype=np.float32).reshape(-1)
            if candidate.size != new_embedding.size:
                continue
            similarity = np.dot(new_embedding, candidate)
            if similarity> best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score
    
    return None, best_score



def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):

    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=30)

        identified_results = {}


        for start, end in segments:

            if (end-start) < sr * 0.5:
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)


            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error(f'Bulk voice processing failed: {e}')
        return {}