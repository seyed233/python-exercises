> 🌐 [Deutsch](README.de.md) | English

# EX5 — Order Validation

An order validation system that checks product IDs, quantities, and stock availability before creating an order.

## Concepts
- `try/except` for error handling
- Input validation (positive numbers, valid IDs)
- Checking stock availability before order creation
- Returning structured data (dictionary) as an order invoice

## Functions
- `get_product_by_id`: Finds a product by its ID
- `get_valid_quantity`: Loops until a valid quantity is entered
- `validate_order`: Raises `ValueError` for invalid orders
- `create_order`: Creates an order dictionary if valid

## How to Run
```bash
python validation.py