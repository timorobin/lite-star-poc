"""Minimal Litestar application."""
from asyncio import sleep
from typing import Any

from litestar import Litestar, get

from pydantic.v1 import BaseModel as V1Model
from pydantic import BaseModel

class V1Payload(V1Model):
    f: str
class V2Payload(BaseModel):
    f: str

@get("/async")
async def async_hello_world() -> dict[str, Any]:
    """Route Handler that outputs hello world."""
    await sleep(0.1)
    return {"hello": "world"}


@get("/sync", sync_to_thread=False)
def sync_hello_world() -> dict[str, Any]:
    """Route Handler that outputs hello world."""
    return {"hello": "world"}


@get("/v1_pydantic", sync_to_thread=False)
def v1() -> V1Payload:
    """Route Handler that outputs hello world."""
    return V1Payload(f="s")


@get("/v2_pydantic", sync_to_thread=False)
def v2() -> V2Payload:
    """Route Handler that outputs hello world."""
    return V2Payload(f="s")


app = Litestar(route_handlers=[sync_hello_world, async_hello_world, v1, v2])
