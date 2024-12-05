from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class NewPost(BaseModel):
    title: str
    author: str


posts = [
    {
        'id': 1,
        'title': 'Python lessons',
        'author': 'Jack Jones'
    },
    {
        'id': 2,
        'title': 'Python practice',
        'author': 'Mark Daniel'
    }
]


@app.get('/', summary='root', tags=['Root routes'])
def root():
    return 'success'


@app.get('/posts', summary='Get posts', tags=['posts'])
def get_posts():
    return posts


@app.get('/posts/{post_id}', summary='Get post by id', tags=['posts'])
def get_post(post_id: int):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post not found')


@app.post('/posts', summary='Create a new post', tags=['posts'])
def create_post(new_post: NewPost):
    posts.append({
        'id': len(posts) + 1,
        'title': new_post.title,
        'author': new_post.author
    })


@app.delete('/posts', summary='Create a new post', tags=['posts'])
def delete_post():
    return

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)
