# Streamlytics: Real-Time Data Analytics Dashboard

Streamlytics is a real-time data analytics platform that collects, processes, and visualizes streaming data. It uses FastAPI for the backend, MySQL for data storage, and Streamlit for the frontend dashboard.

## Features

- Real-time data ingestion from external API
- FastAPI backend for data management
- MySQL database for data storage
- Streamlit dashboard for data visualization
- Dockerized setup for easy deployment

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Git

## Setup

1. Clone the repository:
2. git clone https://github.com/crs7617/Streamlytics.git
cd Streamlytics
Copy
2. Copy the sample environment file and edit it with your credentials:
cp .env.sample .env
CopyEdit the `.env` file with your actual database credentials and API key.

3. Build and run the Docker containers:
docker-compose up -d
Copy
## Project Structure

- `main.py`: FastAPI backend server
- `dashboard.py`: Streamlit dashboard application
- `data-ingestion.py`: Script for fetching and storing data
- `docker-compose.yml`: Docker Compose configuration
- `Dockerfile`: Docker configuration for the web service
- `requirements.txt`: Python dependencies

## Usage

1. Access the FastAPI backend at `http://localhost:80`
2. View the Streamlit dashboard at `http://localhost:8501`
3. API endpoints:
- POST `/data`: Add new data point
- GET `/data`: Retrieve all data points

## Data Ingestion

The `data-ingestion.py` script fetches data from an external API and stores it in the MySQL database. To run it manually:
python data-ingestion.py
Copy
## Development

To run the services individually for development:

1. Start the MySQL database:
docker-compose up db
Copy
2. Run the FastAPI server:
uvicorn main:app --reload
Copy
3. Run the Streamlit dashboard:
streamlit run dashboard.py
Copy
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
