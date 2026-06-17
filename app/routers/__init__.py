from fastapi import APIRouter

from app.routers import auth

# Central place for ALL backend routes.
# Naya router banao to neeche bas ek line add karo:
#   from app.routers import <new_module>
#   api_router.include_router(<new_module>.router)
api_router = APIRouter()

api_router.include_router(auth.router)
