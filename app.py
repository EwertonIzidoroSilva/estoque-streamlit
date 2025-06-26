# app.py
import streamlit as st
import requests

# Configurações da API Supabase
SUPABASE_URL = "https://xhbqtceonstbacfcgidr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhoYnF0Y2VvbnN0YmFjZmNnaWRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA4NjIyMjMsImV4cCI6MjA2NjQzODIyM30.mml3sQJQhCWp_bNYKk7Edff-fBo1PDuqG7SPjw9bNWg"
TABELA = "databaseestoque"

# Leitura do ID da URL
params = st.query_params
item_id = params.get("id", "")

st.title("🔍 Consulta de Item no Estoque")

if item_id:
    st.info(f"Buscando pelo ID: {item_id}")

    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/{TABELA}?ID=eq.{item_id}",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json"
            }
        )

        if response.status_code == 200:
            dados = response.json()
            if dados:
                item = dados[0]
                st.success("Item encontrado com sucesso!")
                st.write(f"**Nome:** {item.get('NOME', '-')}")
                st.write(f"**Código:** {item.get('CÓDIGO', '-')}")
                st.write(f"**Quantidade Atual:** {item.get('QTDE_ATUAL', '-')}")
                st.write(f"**Posição:** {item.get('POSIÇÃO', '-')}")
                st.write(f"**Tipo:** {item.get('TIPO', '-')}")
            else:
                st.error("❌ Item não encontrado no banco de dados.")
        else:
            st.error(f"Erro ao buscar item: {response.text}")

    except Exception as e:
        st.error(f"Erro ao buscar item: {e}")
else:
    st.warning("Por favor, forneça um ID válido na URL.")
