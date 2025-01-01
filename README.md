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
- AWS account with DynamoDB permissions
- Polygon.io API key
- Optionally, `pip` for dependency management

### Clone the Repository
```bash
git clone https://github.com/your-username/auroramarkets.git
cd auroramarkets
---

### Install Python Dependencies

Run the following command to install all required Python dependencies:

```bash
pip install -r requirements.txt
