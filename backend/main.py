from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db/market_data"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

class StockPrice(Base):
    __tablename__ = 'stock_prices'
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)

@app.get("/api/prices/{ticker}")
def get_price(ticker: str):
    db = SessionLocal()
    prices = db.query(StockPrice).filter(StockPrice.ticker == ticker).all()
    return prices

@app.get("/api/predictions/{ticker}")
def get_prediction(ticker: str):
    # Dummy prediction logic
    return {"ticker": ticker, "prediction": "up"}
