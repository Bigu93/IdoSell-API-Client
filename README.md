# IdoSell API Integration Project

This project provides a Python-based integration with the IdoSell eCommerce system, allowing for efficient interaction with the IdoSell API for product management.

## Description

This Python module is designed to streamline operations with the IdoSell API. It includes functionalities such as authenticating with the IdoSell system, fetching product details, and processing responses. The project is useful for developers and businesses looking to integrate their systems with IdoSell for improved eCommerce operations.

## Installation

Clone the repository and install the required dependencies.
```bash
git clone https://github.com/Bigu93/IdoSell-API-Client.git
cd IdoSell-API-Client
pip install -r requirements.txt
```

## Usage

```python
from idosellapi import Auth, BaseClient, create_payload

# Authentication and API client setup
auth = Auth(CLIENT_USERNAME, CLIENT_SECRET, BASE_URL)
token = auth.get_token()
idosellapi = ProductApi(BASE_URL, token)
# Create payload and fetch product details
payload = create_payload(product_ids=[1,2,3], lang_id="eng")
response = idosellapi.get_products(payload)

# Process and use the response
processed_response = process_response(response.data)

product_info = [processed_response]
for product in product_info[0].results:
    print(product.product_id)
```

## Contributing

Contributions to improve this project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request. For significant changes or enhancements, kindly open an issue first to discuss your ideas.

## License

This project is licensed under the GPL-3.0 License - see the [License](https://github.com/Bigu93/IdoSell-API-Client/blob/main/LICENSE)
