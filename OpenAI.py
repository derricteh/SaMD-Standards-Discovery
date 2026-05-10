# Setting up API token in environment
import os
from openai import OpenAI
import streamlit as st
import json


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
def get_response(input):


    prompt = f"""
    You are an expert regulatory and technical analyst specialising in emerging 
    technologies and regulated software systems.

    Your task is to extract structured, compliance-relevant information from a 
    user-provided innovation description.

    Be precise and conservative. Do not infer information that is not explicitly 
    stated. If information is missing or unclear, use null.

    Return ONLY a valid JSON object in exactly this structure, no preamble:

    {
    "product_type": "",
    "brief_description": "",
    "intended_purpose": "",
    "target_users": "",
    "usage_environment": "",
    "core_technologies": "",
    "data_sources": "",
    "data_processing_type": "",
    "deployment_environment": "",
    "system_integrations": "",
    "safety_risks": "",
    "cybersecurity_risks": "",
    "privacy_risks": "",
    "human_in_the_loop": "",
    "regulated_domains": "",
    "possible_classification": "",
    "lifecycle_stages": "",
    "missing_information": ""
    }

    Description:
    {input}
    """

    response = client.responses.create(
        model="gpt-5.4-2026-03-05",
        input=prompt,
        temperature=0
    )
    print_response(response)
    
    return (response)

def print_response(response):
    response = response.output_text.strip()
    data = json.loads(response)
    

    fields = [

        ("Product Type", "product_type"),
        ("Brief Description", "brief_description"),
        ("Intended Purpose", "intended_purpose"),
        ("Target Users", "target_users"),
        ("Usage Environment", "usage_environment"),
        ("Core Technologies", "core_technologies"),
        ("Data Sources", "data_sources"),
        ("Data Processing Type", "data_processing_type"),
        ("Deployment Environment", "deployment_environment"),
        ("System Integrations", "system_integrations"),
        ("Safety Risks", "safety_risks"),
        ("Cybersecurity Risks", "cybersecurity_risks"),
        ("Human-in-the-loop", "human_in_the_loop"),
        ("Regulated Domains", "regulated_domains"),
        ("Possible Classification", "possible_classification"),
        ("Lifecycle Stages", "lifecycle_stages"),
        ("Missing Information", "missing_information")]

    for label, key in fields:
        st.markdown(f"### {label}")
        st.write(data.get(key, "Not available"))

def get_explanations(query, chunk):
    prompt = f"""
    You are an expert in AI-based medical systems and regulatory standards.

    Query:
    {query}

    Retrieved Document:
    {chunk}

    Task:
    1. Extract the most relevant terms or phrases from the document that match the query.
    2. For each term, briefly state why it is relevant (1 short sentence).
    3. Focus on domain-specific concepts (e.g., safety, risk, compliance, clinical use).

    Output format:
    - term: explanation
    - term: explanation
    - term: explanation

    Limit to 3 to 5 items. Be concise.
    """

    response = client.responses.create(
        model="gpt-5.4-2026-03-05",
        input=prompt,
        temperature=0
    )

    
    return (response.output_text.strip())

