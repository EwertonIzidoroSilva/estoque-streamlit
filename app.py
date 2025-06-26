import streamlit as st
from supabase import create_client, Client

# --- Configurações Supabase ---
SUPABASE_URL = "https://xhbqtceonstbacfcgidr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Configurações da Página ---
st.set_page_config(page_title="Consulta de Estoque", page_icon="🔍", layout="centered")
st.title("🔍 Consulta de Item no Estoque")

# --- Leitura do parâmetro da URL ---
query_params = st.query_params
id_param = (query_params.get("id") or query_params.get("ID") or [None])[0]

if id_param:
    id_param = str(id_param).strip()  # Limpa espaços extras

    try:
        response = supabase.table("DATABASEESTOQUE").select("*").eq("ID", id_param).execute()
        item = response.data[0] if response.data else None

        if item:
            st.success("✅ Item encontrado!")
            st.markdown(f"**📦 ID:** `{item.get('ID', 'N/A')}`")
            st.markdown(f"**📝 Descrição:** {item.get('NOME', 'Não informado')}")
            st.markdown(f"**📌 Posição:** {item.get('NUMERO', 'Não definido')}")
            st.markdown(f"**📂 Tipo:** {item.get('TIPO', 'Não definido')}")
            st.markdown(f"**📊 Quantidade Atual:** {item.get('QTDE ATUAL', 'N/A')}")
        else:
            st.error("❌ Item não encontrado no banco de dados.")
    except Exception as e:
        st.error(f"❌ Erro na busca: {e}")
else:
    st.info("⏳ Aguardando leitura do QR Code com parâmetro `id` na URL.")
