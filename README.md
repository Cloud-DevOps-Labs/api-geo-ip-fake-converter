# IP to Coordinates API

A serverless service that converts IP addresses into random GPS coordinates (always on land). Implemented with AWS Lambda and API Gateway.

## Features

- Authentication via API key
- Random coordinates always on land (continents)
- Serverless (AWS Lambda + API Gateway)
- Infrastructure as Code (Terraform)

## Prerequisites

- AWS CLI configured with credentials
- Terraform installed
- Python 3.9 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ip-to-coords-api.git
cd ip-to-coords-api
```

2. (Optional) Modify variables in `terraform/variables.tf`:
- `aws_region`: AWS Region

## Deployment

1. Initialize and apply Terraform configuration:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

2. After completion, get your API credentials:
```bash
terraform output -raw api_key        # Get your API key
terraform output -raw api_endpoint   # Get your API endpoint
terraform output -raw curl_example   # Get a ready-to-use curl command
```

## Usage

The API accepts GET requests with the following parameters:

- `ip`: The IP address to convert
- `api_key`: API key for authentication

### Usage Example

You can get a ready-to-use curl command with:
```bash
terraform output -raw curl_example
```

Or make your own request:
```bash
curl "https://[your-api-id].execute-api.[region].amazonaws.com/coords?ip=1.2.3.4&api_key=[your-api-key]"
```

### Response

```json
{
    "ip": "1.2.3.4",
    "latitude": 45.123456,
    "longitude": -75.987654
}
```

## Project Structure

```
.
├── src/
│   └── lambda_function.py    # Lambda function code
├── terraform/
│   ├── main.tf              # Main Terraform configuration
│   ├── variables.tf         # Terraform variables
│   └── outputs.tf           # Terraform outputs
├── .gitignore
├── LICENSE.md
└── README.md
```

## License

This project is under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
