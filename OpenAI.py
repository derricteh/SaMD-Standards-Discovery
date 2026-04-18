# Setting up API token in environment
import os
from openai import OpenAI
os.environ['OPENAI_API_KEY'] = "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"


def get_response(input):


    client = OpenAI()

    prompt = """
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
    """ + input

    response = client.responses.create(
        model="gpt-5.4-mini-2026-03-17",
        input=prompt,
        temperature=0
    )
    

    return (response)
