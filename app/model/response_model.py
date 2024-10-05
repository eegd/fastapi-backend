from typing import Optional

from pydantic import BaseModel


class InfoRes(BaseModel):
    success: bool
    reason: Optional[str] = None


class InfoUser(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str
