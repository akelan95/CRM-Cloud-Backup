# ** Code Explanation: `data.py`**
This document provides a **detailed, line-by-line breakdown** of `data.py`, explaining every concept in **simple terms**.

--------------------------------------------------------------------------

## **Full Code: `data.py`**
```python
# Step 1: Create a dictionary that acts like a CRM database
customers = {
    101: {"name": "Adam Johnson", "email": "adam.johnson@example.co.uk", "phone": "07911 123456"},
    102: {"name": "Sophie Williams", "email": "sophie.williams@example.co.uk", "phone": "07845 987654"},
    103: {"name": "James O'Connor", "email": "james.oconnor@example.co.uk", "phone": "07722 456789"},
}

# Step 2: Define a function to get customer details by ID
def get_customer_details(customer_id):  # Function definition
    return customers.get(customer_id, "Customer not found")  # Fetches customer info or returns "not found"

# Step 3: Run test cases only if we execute this script directly
if __name__ == "__main__":
    print(get_customer_details(101))  # Expected: Adam Johnson's details
    print(get_customer_details(999))  # Expected: "Customer not found"

--------------------------------------------------------------------------

**Line-by-Line Breakdown**

Step 1 Creating the customers Dictionary (Mock CRM Database)

Full Code for Step 1
```python
customers = {
    101: {"name": "Adam Johnson", "email": "adam.johnson@example.co.uk", "phone": "07911 123456"},
    102: {"name": "Sophie Williams", "email": "sophie.williams@example.co.uk", "phone": "07845 987654"},
    103: {"name": "James O'Connor", "email": "james.oconnor@example.co.uk", "phone": "07722 456789"},
}


Purpose of this code:

This part of the code initially creates a Python dictionary called customers, which acts as my mock CRM database.

Within this dictionary, we have customer IDs (101, 102, 103) as the keys, which represent unique customer records.

Each key's value is a nested dictionary that stores customer details, including:

"name" → Customer’s full name
"email" → Customer’s email address
"phone" → Customer’s phone number

--------------------------------------------------------------------------

Step 2: Defining a Function (def get_customer_details(customer_id))

Full Code for Step 2

def get_customer_details(customer_id):
    return customers.get(customer_id, "Customer not found")

Purpose of this code:

This part of the code defines a function called get_customer_details(), which is responsible for retrieving customer details based on a given customer ID.

How it works:

The function takes a single input parameter, customer_id, which represents a unique customer ID. It then searches for customer_id within the customers dictionary using the .get() method. If the ID exists, the function returns the corresponding customer details. If the ID does not exist, it returns "Customer not found" instead of displaying an error.

Why use .get() Instead of customers[customer_id]?

If we used customers[customer_id] and the ID was not found, Python would crash with a KeyError. The .get(customer_id, "Customer not found") method prevents this error by safely returning a default message instead.

--------------------------------------------------------------------------
Step 3: Explanation Breakdown (if __name__ == "__main__")

Full Code for Step 3

if __name__ == "__main__":
    print(get_customer_details(101))  # Expected output: Adam Johnson's details
    print(get_customer_details(999))  # Expected output: "Customer not found"

Purpose of this code:

This part of the code is used to run test cases and verify that get_customer_details() extracts customer data correctly.

The first test case (101) checks that the function correctly returns Adam Johnson’s details. The second test case (999) ensures that the function correctly returns "Customer not found" when an invalid ID is provided.

Why use if __name__ == "__main__"?

If we execute `python data.py`, Python runs the entire script, including the test cases. However, if `data.py` is imported into another file, we do not want these test cases to run automatically. The condition if __name__ == "__main__" acts as a hard stop, ensuring that the test cases only execute when data.py is run manually.