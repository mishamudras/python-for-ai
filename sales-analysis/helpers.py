# helpers.py

def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return round(quantity * price, 2)

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"