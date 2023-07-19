from fastapi import HTTPException, Query, status

from ..config import settings

"""
TODO: Implement authentication using middleware instead of this function.

This function is deprecated.
It is temporarily enabled for debugging purposes.
Please remove it in the production environment.
"""

def verify_key(
    key: str = Query(
        ...,
        title="Debug Key",
        description="A debug API access key is required.",
        deprecated=True,
    )
) -> str:
    """Verify the key is valid"""
    if key != settings.DEBUG_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid key"
        )
