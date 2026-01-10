# keeping Pricing rules separately, decoupling them from checkout

class PricingRules:
    def __init__(self, unit_price:int, offers:list[dict]=[]):
        self.unit_price = unit_price
        self.unit_offers = offers
    
    def calculate_price(self, unit_count):
        
        #Sorting offers to get max quantity first
        print(self.unit_offers)
        offers = sorted(self.unit_offers, key=lambda x: x.get("quantity"), reverse=True)

        #Applying Offers to get offer related prices for applicable quantities
        remaining_unit_count = unit_count
        offer_unit_price = 0
        for offer in offers:
            offer_quantity_multiple = remaining_unit_count // offer.get("quantity")
            remaining_unit_count = remaining_unit_count % offer.get("quantity")
            offer_unit_price += offer_quantity_multiple *offer.get("price")
        
        #Applying Unit price for any remaining unit which not covered under any offers
        if remaining_unit_count > 0:
            offer_unit_price += remaining_unit_count * self.unit_price
        
        return offer_unit_price



