import os
from fauna import fql
from fauna.client import Client
from fauna.encoding import QuerySuccess
from fauna.errors import FaunaException

# Initialize the client to connect to Fauna
client = Client(secret=os.getenv("FAUNA_KEY"))

try:
    # Compose a query
    query = fql(
        """
        Product.all() {
            name,
            description,
            price
            }"""
    )

    # Run the query
    res: QuerySuccess = client.query(query)
    print(res.data)
except FaunaException as e:
    print(e)
finally:
    # Clean up any remaining resources
    client.close()
