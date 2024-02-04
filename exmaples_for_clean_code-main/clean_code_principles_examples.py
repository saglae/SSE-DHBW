
#Meaningful Variable Names
# Unclean Code
x = 10  # What does 'x' represent?

# Clean Code
total_score = 10  # Clearly indicates the purpose of the variable.



# 2. Avoiding Magic Numbers and Strings:
# Unclean Code
def calculate_price(quantity):
    return quantity * 5.23  # What does 5.23 represent?

# Clean Code
PRICE_PER_UNIT = 5.23

def calculate_price(quantity):
    return quantity * PRICE_PER_UNIT  # Now it's clear what we're multiplying by.


# 3. Functions with a Single Responsibility

