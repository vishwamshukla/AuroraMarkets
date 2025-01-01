# AuroraMarkets

AuroraMarkets is a backend system designed to fetch, store, and serve real-time and historical stock market data using **Polygon.io APIs** and **AWS DynamoDB**. It provides RESTful APIs to access business-critical insights, making it easy to integrate with front-end dashboards or analytics systems.

## Features

- Fetch stock market data from **Polygon.io** APIs.
- Store real-time and historical stock data in **AWS DynamoDB**.
- Expose RESTful APIs for querying and listing stock data.
- Modular architecture for scalability and maintainability.
- Dynamic configuration with environment variables for flexibility.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: AWS DynamoDB
- **API Integration**: Polygon.io
- **Cloud Services**: AWS (DynamoDB, Lambda, EC2, etc.)
- **Tools**: Requests, Boto3, dotenv

---

## Installation

### Prerequisites
- Python 3.8+
- AWS account with CLI and DynamoDB permissions
- Polygon.io API key
- Optionally, `pip` for dependency management

### Clone the Repository
```bash
git clone https://github.com/your-username/auroramarkets.git
cd auroramarkets
```

### Install Python Dependencies

Run the following command to install all required Python dependencies:

```bash
pip install -r requirements.txt
```

### Create a .env in the root

```text
POLYGON_API_KEY=your_polygon_api_key
DYNAMODB_TABLE_NAME=StockData
```
### Run the application

```bash
python app.py
```

## Future Work

### CI/CD Enhancements
- Implement CI/CD pipelines using **Terraform**, **Jenkins**, and **Docker**.
- Deploy and orchestrate using **Kubernetes** for scalability.

### Serverless Architecture
- Transition to a serverless setup using **AWS Lambda** and **API Gateway**.
- Use **S3** and **CloudFront** for static asset delivery.

### Security Enhancements
- Integrate **AWS Secrets Manager** for managing sensitive credentials.
- Add **HTTPS/TLS** for secure API communication.
- Implement authentication with **AWS Cognito** or OAuth.

### Scalability Improvements
- Add **pagination** to endpoints for large datasets.
- Introduce **Redis caching** for frequent API calls.
- Use **DynamoDB Streams** for real-time data updates.

---

## New Features

### Advanced Analytics
- Add endpoints for moving averages, trend predictions, and volume aggregations.

### Notifications and Alerts
- Enable real-time stock alerts via **AWS SNS** (email/SMS).

### Multi-Asset Support
- Expand to include cryptocurrencies and forex using APIs like **CoinGecko**.

### Role-Based Access Control (RBAC)
- Add user roles (e.g., admin, analyst) for restricted API access.

### Historical Data Backfilling
- Support bulk backfilling of historical stock data for analysis.
