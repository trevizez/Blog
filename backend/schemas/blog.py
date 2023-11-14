from datetime import datetime

from pydantic import BaseModel
from pydantic import root_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str | None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace("", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: str | None
    created_at: datetime

    class Config:
        from_attributes = True


class UpdateBlog(CreateBlog):
    pass
