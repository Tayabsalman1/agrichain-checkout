from price_configuration import load_price_configuration
from pricing_rules import PricingRules

class Checkout:
    def __init__(self,):
        self.total = 0
        self.scanned_items = {}
        self.checkout_total = 0
    
    def scan_items(self, items):
        
        # Aggregate the scanned items to get counts
        for item in items.upper():
            if item in self.scanned_items:
                self.scanned_items[item] += 1
            else:
                self.scanned_items[item] = 1
        
        self.load_item_pricing()

        #GEtting price of each item, by applying offers if any
        item_total = 0
        for item in self.scanned_items:
            item_total += self.pricing_config[item].calculate_price(self.scanned_items[item])
        
        self.checkout_total = item_total
    

    def load_item_pricing(self, ):
        """ Loading pricing consfiguration only for the items scanned
            Lets say there are A to Z 26 items are there,
            But the scanned ones are just A, B and C then only 3 pricing configs are fetched"""
        self.pricing_config = load_price_configuration(list(self.scanned_items.keys()))


        

