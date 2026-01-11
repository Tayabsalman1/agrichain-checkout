from price_configuration import load_price_configuration
from pricing_rules import PricingRules

class Checkout:
    def __init__(self,):
        self.total = 0
        self.scanned_items = {}
        self.checkout_total = 0
    
    def scan_items(self, items):
        
        # Aggregate the scammed items to get counts
        for item in items.upper():
            if item in self.scanned_items:
                self.scanned_items[item] += 1
            else:
                self.scanned_items[item] = 1
        
        self.load_item_pricing()
        print(self.pricing_config)

        item_total = 0
        for item in self.scanned_items:
            item_pricing_config = self.pricing_config[item]
            pricing_obj = PricingRules(unit_price=item_pricing_config["unit_price"], offers=[] if "offers" not in item_pricing_config else item_pricing_config["offers"])
            item_total += pricing_obj.calculate_price(self.scanned_items[item])
        
        self.checkout_total = item_total
    

    def load_item_pricing(self, ):
        self.pricing_config = load_price_configuration(list(self.scanned_items.keys()))


        

