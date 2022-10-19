from fastapi import APIRouter
from . import converter


router = APIRouter(prefix='/api/v1')

router.include_router(converter.router)