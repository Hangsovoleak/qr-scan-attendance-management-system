
from services.qr_service import create_qr

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import HttpUrl, ValidationError

app = FastAPI()

# allow react app (vite runs on port 5173 by default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generated-qr")
def generate_qr(url: str = Query(..., description="The URL to convert into a QR code")):
    # validate URL using Pydantic
    try:
        HttpUrl(url)
    except ValidationError:
        raise HTTPException(status_code=400, detail="Invalid URL format. Please enter a valid URL.")

    qr_image = create_qr(url)
    return Response(content=qr_image, media_type="image/png")