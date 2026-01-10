from price_configuration import load_price_configuration

class Checkout:
    def __init__(self,):
        self.total = 0
        self.scanned_items = {}
    
    def scan_items(self, items):
        
        # Aggregate the scammed items to get counts
        for item in items:
            if item in self.scanned_items:
                self.scanned_items[item] += 1
            else:
                self.scanned_items[item] = 1
        
        self.load_item_pricing()
        print(self.pricing_config)
    

    def load_item_pricing(self, ):
        self.pricing_config = load_price_configuration(list(self.scanned_items.keys()))


        

