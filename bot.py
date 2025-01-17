import streamlit as st
from agent.agentorch import AgentOrch
from agent.models import get_model

# Initialize the AgentOrch object
orch = AgentOrch()

def main():
    st.title("🤖 Data Bot")
    st.write("🔍 Chat with your SQL Database")
    
    # Dropdown for model selection
    model_options = {"openai": "gpt4o", "ollama": "ollama_chat/llama3.2", "transformers": "meta-llama/Llama-3.2-3B-Instruct"}
    selected_provider = st.sidebar.selectbox("Select Model Provider", list(model_options.keys()), index=0)
    
    # Prepopulate model ID based on selection
    model_id = model_options[selected_provider]
    model_id = st.sidebar.text_input("Model ID", model_id, key="model_id")
    
    # Call get_model function when selection changes
    if st.sidebar.button("Set Model"):
        model = get_model(selected_provider, model_id)
        orch.set_model(model)

    with st.sidebar:
        prompt_template = orch.get_prompt()
        prompt_template = st.text_area("Prompt Template", prompt_template, height=680)
        
        if st.button("Set Template"):
            st.session_state['prompt_template'] = prompt_template
            orch.set_prompt(prompt_template=prompt_template)
           
    
    user_query = st.text_input("Enter your question", "Find me the customer who bought the most number of tracks drilled down by genre")
    
    if st.button("🛠️ Run Query"):
        with st.spinner("⏳ Querying data..."):
            result = orch.agent_query(query=user_query)
            
            if "error" in result:
                st.error(f"❌ An error occurred: {result['error']}")
            else:
                st.success("✅ Query executed successfully!")
                st.write(result)

if __name__ == "__main__":
    main()
