import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import HTTPBasic
from starlette.middleware.cors import CORSMiddleware

import models
from api.routers import users, mentions, comparison
from database import db_engine

tags_metadata = [
    {
        "name": "User Management",
        "description": "User Integration Api's"

    },
    {
        "name": "Mentions",
        "description": "Mentions Integration Api's"

    },
    {
        "name": "Comparison",
        "description": "Comparison Integration Api's"

    }

]

description = """
MediaMonitoringTool API helps you do awesome stuff
"""

app = FastAPI(
    openapi_tags=tags_metadata,
    title="MediaMonitoringTool",
    description=description,
    version="0.0.1",
    docs_url=None

)

origins = [
    "http://localhost:4200",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(mentions.router)
app.include_router(comparison.router)


@app.get("/docs")
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
