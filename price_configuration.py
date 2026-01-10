import json

def load_price_configuration(items):
    pricing_dict = {}
    with open("pricing_configuration.json", 'r') as file:
        pricing_dict = json.load(file)
    
    missing_pricing = []
    selective_pricing = {}
    for item in items:
        if item not in pricing_dict:
            missing_pricing.append(item)
            continue
        selective_pricing[item] = pricing_dict[item]
    
    if missing_pricing:
        raise Exception(f"Pricing not configured for items {', '.join(missing_pricing)}. Pls Update config")

    return selective_pricing

    
