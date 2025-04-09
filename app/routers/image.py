from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from models.request import ImageGenerationRequest
from services.dalle import generate_image
import uuid
import os

router = APIRouter(
    prefix="/api/images",
    tags=["images"],
    responses={404: {"description": "Not found"}},
)

@router.post("/generate")
async def create_image(request: ImageGenerationRequest):
    try:
        image_result = await generate_image(
            prompt=request.prompt,
            size=request.size,
            n=request.n
        )
        return image_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_models():
    # 這個API端點只返回我們支援的模型，實際上只有DALL-E
    return {
        "models": [
            {"id": "dall-e-3", "name": "DALL-E 3"},
            {"id": "dall-e-2", "name": "DALL-E 2"}
        ]
    }