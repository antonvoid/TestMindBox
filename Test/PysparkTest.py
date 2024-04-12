result = (products_table.join(Link,
    products_table.id == Link.product_id, how='left')
    .join(categories_table,
    Link.category_id == categories_table.id, how='left')
    .select(['product_name', 'category_name'])).show(truncate=True)