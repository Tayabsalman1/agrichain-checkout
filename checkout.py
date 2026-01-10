
class Checkout:
    def __init__(self,):
        self.total = 0
        self.scanned_items = {}
    
    def scan_items(self, items):
        
        # Aggregate the scammed items to get counts
        for item in items:
            if item in self.scanned_items:
                self.scan_items[item] += 1
            else:
                self.scanned_items[item] = 1
        
        self.load_item_pricing()
    

    def load_item_pricing():
        json_data = {
            "A" : {
                "price" : 50,
                "offers" :  [
                    {"quanity" : 2, "price": 90},
                    {"quanity" : 4, "price": 150}
                ]
            },
            "B" : {
                "price" : 100,
                "offers" :  [
                    {"quanity" : 2, "price": 175},
                    {"quanity" : 3, "price": 250}
                ]
            },
            "C" : {
                "price" : 30,
                "offers" :  [
                    {"quanity" : 2, "price": 50},
                    {"quanity" : 4, "price": 90}
                ]
            }
        }

        
        

