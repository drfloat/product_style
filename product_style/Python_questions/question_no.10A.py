product_data = {
    "name": "Lenovo Laptop",
    "default_code": "LP20032",
    "product_uom_id": 12,
}

if 'product_uom_id' in product_data:
    product_data['uom_id'] = product_data.pop('product_uom_id')

print(product_data)