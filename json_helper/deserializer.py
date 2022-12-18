from pydantic import BaseModel, validator, Field
from datetime import datetime
from typing import Optional


class Header(BaseModel):
    table: str
    action_type: str
    from_dict: Optional[bool]
    data_type: str


class CommentsData(BaseModel):
    comment_id: int = Field(alias='id')
    comment_author: str
    timestamp: Optional[int]
    text: str

    @validator('timestamp')
    def set_timestamp(cls, v):
        if not v:
            v = datetime.now().timestamp()
        return v


class ArticleData(BaseModel):
    article_id: int = Field(alias='id')
    article_author: str
    title: str
    timestamp: int
    text: str
    tags: Optional[list[str]]
    comments: Optional[list[int]]
    views: Optional[int]

    @validator('timestamp')
    def set_timestamp(cls, v):
        if not v:
            v = datetime.now().timestamp()
        return v


class UserData(BaseModel):
    user_id: Optional[int] = Field(alias='id')
    login: str
    password: Optional[str]
    posts_read: Optional[list[int]]
    posts_written: Optional[list[int]]
    telegram_id: Optional[int]


class UserMessage(BaseModel):
    headers: Header
    data: UserData
