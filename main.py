import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Fast Food API", description="10 ta mazali taom haqida ma'lumot beruvchi API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 10 ta fast food taomlari ro'yxati
fast_food_menyu = [
    {"id": 1, "nomi": "Gamburger", "turi": "Burgerlar", "narxi": "25,000 UZS", "rasmi": "https://picsum.photos/400/300?random=11"},
    {"id": 2, "nomi": "Chizburger", "turi": "Burgerlar", "narxi": "28,000 UZS", "rasmi": "https://picsum.photos/400/300?random=12"},
    {"id": 3, "nomi": "Mol go'shtli Lavash", "turi": "Lavashlar", "narxi": "30,000 UZS", "rasmi": "https://picsum.photos/400/300?random=13"},
    {"id": 4, "nomi": "Tovuqli Lavash", "turi": "Lavashlar", "narxi": "27,000 UZS", "rasmi": "https://picsum.photos/400/300?random=14"},
    {"id": 5, "nomi": "Pitsa Pepperoni", "turi": "Pitsalar", "narxi": "75,000 UZS", "rasmi": "https://picsum.photos/400/300?random=15"},
    {"id": 6, "nomi": "Pitsa Kombinatsiya", "turi": "Pitsalar", "narxi": "80,000 UZS", "rasmi": "https://picsum.photos/400/300?random=16"},
    {"id": 7, "nomi": "Kartoshka Fri", "turi": "Sneklar", "narxi": "14,000 UZS", "rasmi": "https://picsum.photos/400/300?random=17"},
    {"id": 8, "nomi": "Xot-dog Klasik", "turi": "Xot-doglar", "narxi": "16,000 UZS", "rasmi": "https://picsum.photos/400/300?random=18"},
    {"id": 9, "nomi": "Tovuqli Stripts", "turi": "Sneklar", "narxi": "22,000 UZS", "rasmi": "https://picsum.photos/400/300?random=19"},
    {"id": 10, "nomi": "Koka-Kola 0.5L", "turi": "Ichimliklar", "narxi": "8,000 UZS", "rasmi": "https://picsum.photos/400/300?random=20"}
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