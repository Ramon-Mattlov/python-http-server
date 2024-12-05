from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/', summary='root', tags=['Root routes'])
def root():
    return 'Hello world'


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)

