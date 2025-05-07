# NOVA-SBE-Programming

# Project: Finance Tracker
A simple personal finance dashboard built with **FastAPI** (backend) and **Vue.js** (frontend). Track your income, expenses, and view a visual summary of your finances.

# Authors
- 58327
- 64908
- 65984
- 63923

# Features
- Add income and expense transactions
- See summaries for total income, total expenses, and net balance
- View charts comparing income vs. expenses
- Browse recent transactions
- Clean and responsive interface using Bootstrap 5

# Tech Stack
- **Frontend**: Vue 3, Axios, Chart.js, Bootstrap 5  
- **Backend**: FastAPI, Pydantic  
- **Database**: SQLite  
- **API Server**: Uvicorn  

# Setup & Run Instructions

# 1. Create and activate virtual environment
python -m venv venv && source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 2. Install dependencies
pip install fastapi uvicorn pydantic sqlalchemy

# 3. Start the FastAPI backend
uvicorn main:app --reload  # Runs on http://127.0.0.1:8000

# 4. In a new terminal/tab: Serve the frontend on port 8080
python3 -m http.server 8080  # Visit: http://127.0.0.1:8080/index.html
