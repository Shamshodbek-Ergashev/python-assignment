def typeBasedTransformer(**kwargs):
    transformed = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  
            transformed[key] = value ** 2
        elif isinstance(value, str):  
            transformed[key] = value[::-1]
        elif isinstance(value, bool):  
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):  
            transformed[key] = value[::-1]
        elif isinstance(value, dict):  
            if len(set(value.values())) == len(value): 
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value 
        else:
            transformed[key] = value 

    return transformed


if __name__ == "__main__":
    sample_data = {
        "num": 5,
        "pi": 3.14,
        "text": "Hello",
        "flag": True,
        "items": [1, 2, 3, 4],
        "pairs": {"a": 1, "b": 2},
        "unchanged": set([1, 2, 3]) 
    }

    print(typeBasedTransformer(**sample_data))
