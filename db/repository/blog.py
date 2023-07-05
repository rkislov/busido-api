from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog
from datetime import datetime



def create_new_blog(blog: CreateBlog,db: Session, author_id: int):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    return blogs


def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error": f"Записи с таким id {id} найти не могу"}
    if not blog_in_db.author_id == author_id:
        return {"error": "Только автор может править свой труд"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    blog_in_db.modifed_at = datetime.now()
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error": f"Записи с таким id {id} найти не могу"}
    if not blog_in_db.first().author_id == author_id:
        return {"error": "Только автор может удалить свой труд"}
    blog_in_db.delete()
    db.commit()
    return {"msg":f"удалена запись с id {id}"}
