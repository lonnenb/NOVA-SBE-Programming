from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Literal
from datetime import date
from uuid import uuid4
import sqlite3

DB_PATH = "finance.db"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    id: str
    category: str
    amount: float
    date: date
    type: Literal["income", "expense"]
    recurring: bool

class TransactionCreate(BaseModel):
    category: str
    amount: float
    date: date
    type: Literal["income", "expense"]
    recurring: bool

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id TEXT PRIMARY KEY,
                category TEXT,
                amount REAL,
                date TEXT,
                type TEXT CHECK(type IN ('income','expense')),
                recurring INTEGER
            )
        """)
        print("[INFO] Database initialized and table verified.")

        # Check if data already exists
        cur = conn.execute("SELECT COUNT(*) FROM transactions")
        count = cur.fetchone()[0]
        print(f"[INFO] Number of stored transactions: {count}")

init_db()

@app.post("/transactions/", response_model=Transaction)
def add_transaction(tx: TransactionCreate):
    tx_id = str(uuid4())
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?)",
            (tx_id, tx.category, tx.amount, tx.date.isoformat(), tx.type, int(tx.recurring))
        )
    return Transaction(id=tx_id, **tx.dict())

@app.get("/summary/totals")
def summary_totals():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
        data = dict(cur.fetchall())
    return {"income": data.get("income", 0), "expense": data.get("expense", 0)}

@app.get("/transactions/", response_model=List[Transaction])
def list_transactions():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT * FROM transactions ORDER BY date DESC")
        rows = cur.fetchall()
    return [Transaction(id=row[0], category=row[1], amount=row[2], date=row[3], type=row[4], recurring=bool(row[5])) for row in rows]
