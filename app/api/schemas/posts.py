from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class PostBase(BaseModel):
    content: Optional[str] = None
    user_name: str
    likes: List[str] = []

# Schema for creating a new post
class PostCreate(PostBase):
    pass  # No extra fields are required beyond PostBase

class PostUpdate(PostBase):
    pass  # No extra fields are required beyond PostBase

# Schema for responding with post data
class PostResponse(PostBase):
    id: str
    email: Optional[EmailStr] = None
    date: datetime

    class Config:
        orm_mode = True
