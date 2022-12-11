import yaml


def get_config(file_name):
    with open(file_name, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise Exception("error loading yaml", file_name, e)

