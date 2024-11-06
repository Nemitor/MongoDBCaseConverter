import json

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def convert_dict_keys_to_camel_case(d):
    if isinstance(d, dict):
        return {
            snake_to_camel(k) if k not in ['__v', '_id'] else k: convert_dict_keys_to_camel_case(v)
            for k, v in d.items()
        }
    elif isinstance(d, list):
        return [convert_dict_keys_to_camel_case(i) for i in d]
    else:
        return d

def convert_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    converted_data = convert_dict_keys_to_camel_case(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, ensure_ascii=False, indent=4)

input_json_file = 'input.json'
output_json_file = 'output.json'
convert_json_file(input_json_file, output_json_file)
