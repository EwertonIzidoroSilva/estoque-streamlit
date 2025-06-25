import streamlit as st
from supabase import create_client, Client
import os

# Configurações
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# Pega o parâmetro da URL
query_params = st.query_params
item_id = str(query_params.get("id", [""])[0])

st.title("🔍 Consulta de Item no Estoque")

if item_id:
    try:
        response = supabase.table("DATABASEESTOQUE").select("*").eq("ID", item_id).execute()
        data = response.data

        if data:
            item = data[0]
            st.success("Item encontrado!")
            st.write(f"**ID**: {item['ID']}")
            st.write(f"**Código**: {item['CÓDIGO']}")
            st.write(f"**Nome**: {item['NOME']}")
            st.write(f"**Quantidade em Estoque**: {item['QTDE ATUAL']}")
            st.write(f"**Reservada**: {item['RESERVADA']}")
            st.write(f"**Posição**: {item['POSIÇÃO']}")
        else:
            st.error("Item não encontrado.")
    except Exception as e:
        st.error(f"Erro ao consultar o banco de dados: {e}")
else:
    st.warning("Nenhum ID informado na URL.")
