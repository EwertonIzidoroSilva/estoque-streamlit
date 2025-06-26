import streamlit as st
from supabase import create_client, Client

# --- Configurações do Supabase ---
SUPABASE_URL = "https://xhbqtceonstbacfcgidr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhoYnF0Y2VvbnN0YmFjZmNnaWRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA4NjIyMjMsImV4cCI6MjA2NjQzODIyM30.mml3sQJQhCWp_bNYKk7Edff-fBo1PDuqG7SPjw9bNWg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Página ---
st.set_page_config(page_title="Consulta de Estoque", page_icon="📦")
st.markdown("<h1 style='text-align: center;'>📦 Consulta de Item no Estoque</h1>", unsafe_allow_html=True)

# --- Leitura do parâmetro da URL, aceitando "id" ou "ID"
query_params = st.query_params
id_param = query_params.get("ID", [None])[0] or query_params.get("id", [None])[0]

if id_param:
    try:
        resultado = supabase.table("DATABASEESTOQUE").select("*").eq("ID", id_param).execute()
        dados = resultado.data

        if dados:
            item = dados[0]
            st.success("✅ Item encontrado no estoque!")

            st.markdown(f"**🆔 ID**: {item.get('ID')}")
            st.markdown(f"**📘 Nome/Descrição**: {item.get('NOME')}")
            st.markdown(f"**📍 Posição**: {item.get('POSICAO')}")
            st.markdown(f"**📦 Quantidade Atual**: {item.get('QTDE_ATUAL')}")
            st.markdown(f"**📂 Tipo de Estoque**: {item.get('TIPO')}")

        else:
            st.error("❌ Item não encontrado no banco de dados.")

    except Exception as e:
        st.error(f"⚠️ Erro ao consultar o banco de dados: {e}")
else:
    st.info("🔎 Informe um ID na URL para realizar a consulta.\n\nExemplo:\n`?id=21168304736`")
