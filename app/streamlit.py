import streamlit as st
from src.app.main import run

def main():
  st.set_page_config(
    page_title="Crew Professor CASD",
    page_icon="👨‍🏫",
    layout="wide",
  )

  st.title("👨‍🏫 Crew Professor CASD")

  if "messages" not in st.session_state:
    st.session_state["messages"] = [] 

  # Campo de entrada para o usuário
  with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Digite o tema da aula que você deseja criar:", "")
    submitted = st.form_submit_button("Enviar")
    
  
  # Processamento da entrada do usuário
  if submitted and user_input:
    # Exibir mensagem do usuário no chat
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Executar a equipe de agentes
    with st.spinner("⏳ Processando com os agentes..."):
        result = run(inputs={"main topic": user_input})

    # Exibir a resposta da equipe
    st.session_state["messages"].append({"role": "crew", "content": result})

  # Exibir o histórico de mensagens no chat
  for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f"**Você:** {message['content']}")
    else:
        st.markdown(f"**Equipe de Agentes:**\n\n{message['content']}")


if __name__ == "__main__":
    main()