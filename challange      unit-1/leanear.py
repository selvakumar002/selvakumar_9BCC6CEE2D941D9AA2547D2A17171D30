Def linear_search_product(product_list, target_product):
    Indices = []
    
    For index, product in enumerate(product_list):
        If product == target_product:
            Indices.append(index)
    
    Return indices


Products = [“Apple”, “Banana”, “Orange”, “Pappya”, “Apple”]
Target = “Apple”
Result = linear_search_product(products, target)
Print(f”Indices of ‘{target}’ found in the list: {result}”)
