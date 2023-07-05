from typing import Optional
from slugify import slugify
from pydantic import BaseModel, root_validator
from datetime import date


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values and 'slug' not in values:
            values['slug'] = slugify(values.get("title")).lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date
    modifed_at: date

    class Config():
        orm_mode = True