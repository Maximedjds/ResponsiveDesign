import streamlit as st
from pathlib import Path

# 1. Configuration de la page
st.set_page_config(page_title="McFlow - Landing Page", layout="wide")

# 2. Lecture des fichiers (Note bien : il n'y a plus de dossiers "html/" ou "style/")
try:
    # On lit index.html qui est juste à côté
    html_content = Path("index.html").read_text(encoding="utf-8")
    
    # On lit style.css qui est juste à côté
    # ⚠️ IMPORTANT : Vérifie que ton fichier s'appelle bien "style.css" (sans 's' ou avec 's' selon ton choix)
    css_content = Path("style.css").read_text(encoding="utf-8")
    
    # 3. On mélange le CSS et le HTML pour l'affichage
    full_code = f"<style>{css_content}</style>{html_content}"
    
    # 4. On affiche le tout
    st.components.v1.html(full_code, height=1200, scrolling=True)

except FileNotFoundError as e:
    st.error(f"Erreur : Impossible de trouver le fichier. Vérifie tes noms de fichiers ! Détail : {e}")