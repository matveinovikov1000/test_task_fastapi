from pydantic import BaseModel, HttpUrl


class AddURL(BaseModel):
    url: HttpUrl


class ShortIdURL(BaseModel):
    id: int
    url: HttpUrl
    short_url: str
