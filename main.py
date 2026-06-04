import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Fast Food API", description="10 ta mazali taom haqida ma'lumot beruvchi API")

# Brauzerda frontend bilan muammosiz ulanishi uchun CORS sozlamasi
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 10 ta fast food taomlari ro'yxati (Aniq va chiroyli rasmlar bilan)
fast_food_menyu = [
    {
        "id": 1, 
        "nomi": "Gamburger", 
        "turi": "Burgerlar", 
        "narxi": "25,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop"
    },
    {
        "id": 2, 
        "nomi": "Chizburger", 
        "turi": "Burgerlar", 
        "narxi": "28,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&h=300&fit=crop"
    },
    {
        "id": 3, 
        "nomi": "Mol go'shtli Lavash", 
        "turi": "Lavashlar", 
        "narxi": "30,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1626700051175-6518c4793f4f?w=400&h=300&fit=crop"
    },
    {
        "id": 4, 
        "nomi": "Tovuqli Lavash", 
        "turi": "Lavashlar", 
        "narxi": "27,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1562967914-608f82629a7a?w=400&h=300&fit=crop"
    },
    {
        "id": 5, 
        "nomi": "Pitsa Pepperoni", 
        "turi": "Pitsalar", 
        "narxi": "75,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400&h=300&fit=crop"
    },
    {
        "id": 6, 
        "nomi": "Pitsa Kombinatsiya", 
        "turi": "Pitsalar", 
        "narxi": "80,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&h=300&fit=crop"
    },
    {
        "id": 7, 
        "nomi": "Kartoshka Fri", 
        "turi": "Sneklar", 
        "narxi": "14,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&h=300&fit=crop"
    },
    {
        "id": 8, 
        "nomi": "Xot-dog Klasik", 
        "turi": "Xot-doglar", 
        "narxi": "16,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1619740455993-9e612b1af08a?w=400&h=300&fit=crop"
    },
    {
        "id": 9, 
        "nomi": "Tovuqli Stripts", 
        "turi": "Sneklar", 
        "narxi": "22,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=400&h=300&fit=crop"
    },
    {
        "id": 10, 
        "nomi": "Koka-Kola 0.5L", 
        "turi": "Ichimliklar", 
        "narxi": "8,000 UZS", 
        "rasmi": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400&h=300&fit=crop"
    }
]

@app.get("/")
def home():
    return {"message": "Fast Food API-siga xush kelibsiz! Taomlarni ko'rish uchun /fastfood sahifasiga o'ting."}

@app.get("/fastfood")
def get_menu():
    """Barcha 10 ta fast food taomlarini qaytaruvchi GET methodi"""
    return {"status": "success", "data": fast_food_menyu}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)