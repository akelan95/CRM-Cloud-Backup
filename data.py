# data.py - Mock CRM Database

# Simulating a CRM system using a Python Dictionary
customers = {
    101: {"name": "Adam Johnson", "email": "adam.johnson@example.co.uk", "phone": "07911 123456"},
    102: {"name": "Sophie Williams", "email": "sophie.williams@example.co.uk", "phone": "07845 987654"},
    103: {"name": "James O'Connor", "email": "james.oconnor@example.co.uk", "phone": "07722 456789"},
}

# Function to retrieve customer details
def get_customer_details(customer_id):
    """
    Fetches customer details based on the provided customer ID.

    Parameters:
        customer_id (int): The unique ID of the customer to be retrieved.

    Returns:
        dict or str: If the customer exists, returns their details (dictionary).
                     If the ID does not exist, returns a string "Customer not found".
    """
    return customers.get(customer_id, "Customer not found")

# Testing the function
if __name__ == "__main__":
    print(get_customer_details(101))  # Expected output: Adam Johnson's details
    print(get_customer_details(999))  # Expected output: "Customer not found"
