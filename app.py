import streamlit as st
from supabase import create_client, Client

# Chaves do Supabase
url = "https://<SEU-PROJETO>.supabase.co"
key = "sua_chave_anon_publica"
supabase: Client = create_client(url, key)

# Layout
st.title("🔍 Consulta de Item no Estoque")

# Pega o ID da URL
query_params = st.experimental_get_query_params()
id_param = query_params.get("id", [None])[0]

if id_param:
    st.info(f"Buscando pelo ID: {id_param}")
    try:
        response = supabase.table("databaseestoque").select("*").eq("ID", id_param).execute()
        if response.data:
            item = response.data[0]
            st.success("✅ Item encontrado:")
            st.write(f"**Descrição:** {item['NOME']}")
            st.write(f"**Código:** {item['CÓDIGO']}")
            st.write(f"**Quantidade Atual:** {item['QTDE ATUAL']}")
        else:
            st.error("❌ Item não encontrado no banco de dados.")
    except Exception as e:
        st.error(f"Erro ao buscar item: {e}")
else:
    st.warning("🔗 Nenhum ID fornecido na URL.")
