from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from db.sessions import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog, retreive_blog, list_blogs
from typing import List


router = APIRouter()


@router.post("/blog", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db,author_id=1)
    return blog


@router.get("/blog/{id}", response_model=ShowBlog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Запись блога с id {id} не существует", status_code=status.HTTP_404_NOT_FOUND)
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
async def get_all_published(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs