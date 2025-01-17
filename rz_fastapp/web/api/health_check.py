from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/health")
def health_check() -> dict[str, str]:
    """Checks the health of a project.

    It returns 200 if the project is healthy
    """
    return {"message": "Hello world"}
