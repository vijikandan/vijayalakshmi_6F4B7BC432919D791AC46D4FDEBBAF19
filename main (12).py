"""
Write a function called Linear _seach_product that take the list of products and a target product
name as input. The function should perform a linear search to find the target product in tha list and
return a list of indices of all occurrence of the product if found, or an empty list if the product is not
found.
"""


def LinearSearchProduct(productList , targetProduct):
  indices  = []

for index, Product in enumerate(productList):
 if product ==targetProduct:
  indices.append(index) 

return indices


# Example stage :
products = [ "shoes", " boot", "loafer", "shoes", "sandal", " shoes"]
target = "shoes"
result =LinearSearchProduct(product, target) 
print(result)