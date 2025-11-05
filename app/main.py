from typing import Union
from fastapi import FastAPI
from ytmusicapi import YTMusic, OAuthCredentials
from app.config import settings

ytmusic = YTMusic(
    'oauth.json',
    oauth_credentials=OAuthCredentials(
        client_id=settings.ytmusic_client_id,
        client_secret=settings.ytmusic_client_secret
    )
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, Union[int, str, None]]:
    return {"item_id": item_id, "q": q}
