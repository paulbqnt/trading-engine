from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Order, tags=["orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # db_order = crud.get_order_by_isin(db, isin=order.isin)
    return crud.create_order(db=db, order=order)

@router.get("/", response_model=list[schemas.Order], tags=["orders"])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders