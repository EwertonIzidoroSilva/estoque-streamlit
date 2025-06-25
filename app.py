import streamlit as st
import pandas as pd
from supabase import create_client

SUPABASE_URL = "https://xhbqtceonstbacfcgidr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhoYnF0Y2VvbnN0YmFjZmNnaWRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA4NjIyMjMsImV4cCI6MjA2NjQzODIyM30.mml3sQJQhCWp_bNYKk7Edff-fBo1PDuqG7SPjw9bNWg"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Consulta de Estoque", page_icon="📦")
st.title("🔎 Consulta de Item no Estoque")

item_id = st.query_params.get("id")
if item_id:
    result = supabase.table("DATABASEESTOQUE").select("*").eq("ID", int(item_id)).execute()
    if result.data:
        item = result.data[0]
        st.success("Item encontrado!")
        st.write(f"**ID**: {item['ID']}")
        st.write(f"**Código**: {item['CÓDIGO']}")
        st.write(f"**Nome**: {item['NOME']}")
        st.write(f"**Quantidade em Estoque**: {item['QTDE ATUAL']}")
        st.write(f"**Tipo de Estoque**: {item['TIPO']}")
    else:
        st.error("❌ Item não encontrado.")
else:
    st.info("🛈 Use a URL assim: `?id=200641838107`")
