from pydantic import BaseModel, Field
from typing import Optional, List
from config import DEFAULT_IMAGE_SIZE

class ImageGenerationRequest(BaseModel):
    prompt: str = Field(..., description="用於生成圖像的文字描述")
    size: str = Field(default=DEFAULT_IMAGE_SIZE, description="圖像尺寸 (例如: 1024x1024)")
    n: int = Field(default=1, description="要生成的圖像數量", ge=1, le=10)
    model: str = Field(default="dall-e-3", description="使用的模型")