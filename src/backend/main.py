from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# пользовательский импорт
from app.routers import task, list_item
from fastapi.responses import HTMLResponse
app = FastAPI()

app.include_router(list_item.router)
app.include_router(task.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/color', tags=['colors'])
def get_colors():
    return [
        '#F48FB1',
        '#BA68C8',
        '#64B5F6',
        '#4DD0E1',
        '#00897B',
        '#DCE775',
    ]


