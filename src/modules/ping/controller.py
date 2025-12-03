from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/ping", status_code=200)
async def ping():
    """Liveness check endpoint."""

    return {"message": "Service is running"}
