import streamlit as st
from supabase import create_client, Client
import os

# --- Configurações Supabase ---
SUPABASE_URL = "https://xhbqtceonstbacfcgidr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhoYnF0Y2VvbnN0YmFjZmNnaWRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA4NjIyMjMsImV4cCI6MjA2NjQzODIyM30.mml3sQJQhCWp_bNYKk7Edff-fBo1PDuqG7SPjw9bNWg"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Configurações da Página ---
st.set_page_config(page_title="Consulta de Estoque", page_icon="🔍", layout="centered")

st.title("🔍 Consulta de Item no Estoque")

# --- Leitura do parâmetro da URL, forçando como texto ---
query_params = st.query_params
id_param = str(query_params.get("ID", [None])[0] or query_params.get("id", [None])[0])

if id_param:
    try:
        # Buscar item pelo ID (como texto)
        response = supabase.table("DATABASEESTOQUE").select("*").eq("ID", id_param).execute()
        item = response.data[0] if response.data else None

        if item:
            st.success("✅ Item encontrado!")
            st.markdown(f"**📦 ID:** `{item['ID']}`")
            st.markdown(f"**📝 Descrição:** {item.get('NOME', 'Não informado')}")
            st.markdown(f"**📌 Posição:** {item.get('NUMERO', 'Não definido')}")
            st.markdown(f"**📂 Tipo:** {item.get('TIPO', 'Não definido')}")
            st.markdown(f"**📊 Quantidade Atual:** {item.get('QTDE ATUAL', 'N/A')}")
        else:
            st.error("❌ Item não encontrado no banco de dados.")
    except Exception as e:
        st.error(f"Erro ao buscar item: {e}")
else:
    st.info("⏳ Aguardando leitura de QR Code com parâmetro `id` na URL...")
