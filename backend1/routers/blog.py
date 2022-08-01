from typing import List
from webbrowser import get
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from database import get_db
from repository import blog
from oauth import get_current_user
import schemas, database, models


router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(database.get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return blog.get_all(db)
    # blogs=db.query(models.Blog).all()
    # return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session=Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.create(db, request)
    # new_blog=models.Blog(title=request.title,body=request.body, user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return blog.destroy(id,db)
    # db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    # db.commit()

    # return {'details':'Blog with {id} deleted sucessfully'}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db:Session=Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.update(id, request, db)
    # blog=db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog wit id{id} nod found")
    # blog.update(request)
    # db.commit()
    # return 'updated'
 

 
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id:int, db:Session=Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.show(id,db)
