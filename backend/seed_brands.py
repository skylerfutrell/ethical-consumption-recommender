from backend.database import SessionLocal, Brand

db = SessionLocal()

# Adding some "Initial Data" to test the Recommender
initial_brands = [
    Brand(name="FastStyle", category="Apparel", ethics_score=1.5, description="Low-cost mass production"),
    Brand(name="EcoThreads", category="Apparel", ethics_score=4.8, description="Organic cotton, fair wages"),
    Brand(name="UrbanFit", category="Apparel", ethics_score=3.2, description="Standard mall brand"),
    Brand(name="GlobalTech", category="Tech", ethics_score=2.8, description="Standard hardware manufacturer"),
    Brand(name="GreenCircuit", category="Tech", ethics_score=4.9, description="Recycled components, carbon neutral")
]

db.add_all(initial_brands)
db.commit()
db.close()
print("Database Seeded Successfully!")