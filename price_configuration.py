import json
from pricing_rules import PricingRules
from offer import Offer

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
        
        if "offers" not in pricing_dict[item]:
            pricing_dict[item]["offers"] = []
        
        selective_pricing[item] = PricingRules(
            unit_price=pricing_dict[item]["unit_price"],
            offers=[Offer(quantity=off.get("quantity"), price=off.get("price")) for off in pricing_dict[item]["offers"]]
        ) 
    
    if missing_pricing:
        raise Exception(f"Pricing not configured for items {', '.join(missing_pricing)}. Pls Update config")

    return selective_pricing

    
