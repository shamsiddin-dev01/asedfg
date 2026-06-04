import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mashinalar API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mashinalar = [
    {"id": 1, "nomi": "Chevrolet", "modeli": "Malibu 2", "narxi": "25,000 USD", "rasmi": "https://picsum.photos/400/300?random=1"},
    {"id": 2, "nomi": "Chevrolet", "modeli": "Gentra", "narxi": "13,000 USD", "rasmi": "https://picsum.photos/400/300?random=2"},
    {"id": 3, "nomi": "BYD", "modeli": "Song Plus", "narxi": "30,000 USD", "rasmi": "https://picsum.photos/400/300?random=3"},
    {"id": 4, "nomi": "BYD", "modeli": "Chazor", "narxi": "22,000 USD", "rasmi": "https://picsum.photos/400/300?random=4"},
    {"id": 5, "nomi": "Kia", "modeli": "K5", "narxi": "32,000 USD", "rasmi": "https://picsum.photos/400/300?random=5"},
    {"id": 6, "nomi": "Hyundai", "modeli": "Elantra", "narxi": "24,000 USD", "rasmi": "https://picsum.photos/400/300?random=6"},
    {"id": 7, "nomi": "Toyota", "modeli": "Camry", "narxi": "38,000 USD", "rasmi": "https://picsum.photos/400/300?random=7"},
    {"id": 8, "nomi": "Tesla", "modeli": "Model 3", "narxi": "40,000 USD", "rasmi": "https://picsum.photos/400/300?random=8"},
    {"id": 9, "nomi": "BMW", "modeli": "M5", "narxi": "95,000 USD", "rasmi": "https://picsum.photos/400/300?random=9"},
    {"id": 10, "nomi": "Mercedes-Benz", "modeli": "S-Class", "narxi": "120,000 USD", "rasmi": "https://picsum.photos/400/300?random=10"}
]

@app.get("/")
def home():
    return {"message": "Mashinalar API-siga xush kelibsiz! /cars sahifasiga o'ting."}

@app.get("/cars")
def get_cars():
    return {"status": "success", "data": mashinalar}

# Render portni o'zi berganda adashmasligi uchun ushbu qism muhim
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)