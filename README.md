# Learnosity FastAPI Project

This project implements a FastAPI application that integrates with the Learnosity SDK to provide endpoints for getting and creating items.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Features

- FastAPI backend for efficient API development
- Integration with Learnosity SDK
- Endpoints for getting and creating Learnosity items
- Easy to set up and extend

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7+
- pip (Python package manager)
- A Learnosity account with valid credentials

## Installation

### Clone the repository:
```
git clone https://github.com/muathejamil17/learno-api.git
cd learno-api
```

### Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the required packages:
```
pip install -r requirements.txt
```

## Configuration

### Set up environment variables:
Create a `.env` file in the project root and add your Learnosity credentials:
```
CONSUMER_KEY=ur_consumer_Learnosity_key
CONSUMER_SECRET=ur_consumer_Learnosity_secret
DOMAIN=domain
DATA_BASE_URL=base_data_url_endpoint_url
ORGANIZATION_ID=your_organization_id
```

### Additional configuration:
Adjust any other configuration settings in `config.py` if needed.

## Usage

### Running the server:
To run the FastAPI server:

```
make run
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Get Questions
- `GET /questions/{item_reference}`: Retrieve a items in specific reference
- `curl --location 'http://localhost:8000/questions/{reference_id}?organization_id=<org_id>&tags=<type>:<name>'`
### Create Question
- `POST /questions`: Create a new Learnosity item

For detailed API documentation, visit `http://localhost:8000/docs` after starting the server.
