# Write a function assigning buyers to sellers based on their requests for specific items, given two dictionaries:
#   one for sellers with their available items 
#   one for buyers with their requested items. 



sellers = {
  "seller1" : ["jeans", "t-shirt"],
  "seller2" : ["skirt", "dress"],
  "seller3" : ["coat"]
}

buyersRequests = {
  "buyer1" : "skirt",
  "buyer2" : "jeans",
  "buyer3" : "coat",
  "buyer4" : "skirt"
}


def assign_buyer_to_seller(sellers, buyersRequests):
    buyer_to_seller = {}
    for buyer, requested_item in buyersRequests.items():
        for seller, item_for_sale in sellers.items():
            if requested_item in item_for_sale:
                buyer_to_seller[buyer] = seller
                break
    return buyer_to_seller

print("\n")
print(assign_buyer_to_seller(sellers, buyersRequests))
print("\n")




# output = {
#   "buyer1" : "seller2",
#   "buyer2" : "seller1",
#   "buyer3" : "seller3",
#   "buyer4" : "seller2"
# }