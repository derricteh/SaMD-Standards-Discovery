import streamlit as st
from openai import OpenAI
import tiktoken
from OpenAI import get_response
from embedding import generate_embeddings
from topk import generate_topk
# from embeddings import get_embeddings

def run_streamlit():
   
    st.title('SaMD Standards Discovery')
    openai_api_key = st.sidebar.text_input('OpenAI API Key')

    with st.form('my_form'):
        description_box = st.text_area('Enter Description Here:', placeholder='Enter detailed description here')
        submitted = st.form_submit_button('Submit')
        st.empty()
        response = get_response(openai_api_key, description_box)
        # st.json(response.output_text)

        with open('output.json', 'w') as f:
            print (response.output_text, file = f)

    if submitted:
   
        # st.write(response.output_text)
        st.write("Input tokens:", response.usage.input_tokens)
        st.write("Output tokens:", response.usage.output_tokens)
        st.write("Total tokens:", response.usage.total_tokens)
    #     st.write("Embeddings", get_embeddings(response.output_text))

        # embeddings for dataset
        generate_embeddings()

        generate_topk(k=10)





# # Function to count tokens 
# def count_tokens(string: str) -> int:
#     encoding_name = "p50k_base"
#     encoding = tiktoken.get_encoding(encoding_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens


# def generate_response(input_text):
#     try:
#         llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#         response = llm(input_text)
#         num_tokens = count_tokens(input_text)
#         st.info(f"Input contains {num_tokens} tokens.")
#         st.info(response)
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
   run_streamlit()

    