from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, Brand

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Ethical Recommender Engine is Online"}

@app.get("/recommend/{brand_name}")
def get_recommendation(brand_name: str, db: Session = Depends(get_db)):
    # 1. Look up the brand the user is currently using
    user_brand = db.query(Brand).filter(Brand.name.ilike(brand_name)).first()
    
    if not user_brand:
        raise HTTPException(status_code=404, detail="Brand not found in our ethics database.")

    # 2. THE RECOMMENDER LOGIC:
    # Find brands in the same category with a HIGHER ethics score
    better_options = db.query(Brand).filter(
        Brand.category == user_brand.category,
        Brand.ethics_score > user_brand.score
    ).order_by(Brand.ethics_score.desc()).all()

    return {
        "searched_brand": user_brand.name,
        "current_score": user_brand.ethics_score,
        "recommendations": better_options if better_options else "You are using the most ethical brand in this category!"
    }