import yaml

parti = {
    'test': 1,
    'test2': [1,2,3],
    'test3': {'a':1,'b':2,'c':3}
}


print(yaml.dump(parti, default_flow_style=False ))