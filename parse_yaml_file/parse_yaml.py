import yaml

def get_config(filename, env, obj):
    with open(filename) as file:
        doc = yaml.load(file, Loader=yaml.FullLoader)
        return doc.get(env).get(obj)

print(get_config('./.auth-dev.yaml', 'dev', 'client_id'))