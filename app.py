import json, re
from pathlib import Path
import numpy as np
import streamlit as st
import tensorflow as tf

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "lstm_label_komen.keras"
LABEL_PATH = BASE_DIR / "labels.json"


def clean_text(s: str) -> str:
    s = str(s).lower()
    s = re.sub(r"http\\S+|www\\.\\S+", " ", s)
    s = re.sub(r"@\\w+", " ", s)
    s = re.sub(r"#\\w+", " ", s)
    s = re.sub(r"[^a-z0-9\\s]", " ", s)
    s = re.sub(r"\\s+", " ", s).strip()
    return s

@st.cache_resource
def load_assets():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model tidak ditemukan: {MODEL_PATH}")
    if not LABEL_PATH.exists():
        raise FileNotFoundError(f"labels.json tidak ditemukan: {LABEL_PATH}")

    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    with open(LABEL_PATH, "r", encoding="utf-8") as f:
        labels = json.load(f)
    return model, labels

st.set_page_config(page_title="Dashboard Sentimen LSTM", layout="wide")
st.title(" Dashboard Sentimen (LSTM)")
st.caption("Load model dari Google Drive (tanpa training ulang)")

model, labels = load_assets()

text = st.text_area("Masukkan komentar:", height=140, placeholder="contoh: bagus banget pelayanannya")
do_clean = st.checkbox("Gunakan cleaning seperti training", value=True)
show_probs = st.checkbox("Tampilkan probabilitas semua kelas", value=True)

if st.button("Prediksi"):
    if not text.strip():
        st.warning("Teks masih kosong.")
    else:
        x = clean_text(text) if do_clean else text
        probs = model.predict(np.array([x], dtype=object), verbose=0)[0]
        idx = int(np.argmax(probs))
        st.success(f"Prediksi: **{labels[idx]}** | Confidence: **{float(probs[idx]):.3f}**")

        if show_probs:
            st.subheader("Probabilitas per kelas")
            order = np.argsort(-probs)
            for i in order:
                st.write(f"- {labels[i]}: {float(probs[i]):.4f}")
