from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.services.dashboard_service import get_dashboard_stats

router = APIRouter()


@router.get("/")
def get_dashboard(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)