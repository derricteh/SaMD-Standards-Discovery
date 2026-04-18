import re
import json


def truncate(value, max_length = 15):
    word = value.split()

    if len(word) > max_length:
        return " ".join(word[:max_length])
    else:
        return value


def split(value):
    result = []
    parts = re.split(r'[;,\n]', value)

    for part in parts:
        strip = part.strip()
        if strip:
            result.append(strip)

    return result




def generate_subqueries(queries):


    template = {
    "product_type":           "regulatory standards for {}",
    "core_technologies":      "standards for {}",
    "data_sources":           "standards for health data from {}",
    "deployment_environment": "cybersecurity standards for {} health software",
    "system_integrations":    "interoperability standards for {}",
    "safety_risks":           "risk management standards {}",
    "cybersecurity_risks":    "cybersecurity standards {}",
    "privacy_risks":          "data privacy standards {}",
    "regulated_domains":      "compliance standards for {}",
    "lifecycle_stages":       "software {} standards medical device"}

    split_fields = {
    "core_technologies",
    "data_sources", 
    "lifecycle_stages",
    "regulated_domains"}

    sub_query = []

    for field, field_value in template.items():
        value = queries.get(field)

        if not value or value.lower() in ('not specified', 'null', 'none'):
            continue
        if field in split_fields:
            parts = split(value)
            for part in parts: 
                truncated = truncate(part)
                sub_query.append(field_value.format(truncated))
        else:
            truncated = truncate(value)
            sub_query.append(field_value.format(truncated))

    return sub_query



def generate():
    file_path = 'output.json'

    with open(file_path, 'r') as file:
        user_input = json.load(file)
    subqueries = generate_subqueries(user_input)
    return subqueries




    