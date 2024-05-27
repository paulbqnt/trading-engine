from typing import Union, List, Optional
from pydantic import BaseModel, Field
from datetime import date
from uuid import UUID, uuid4

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: Optional[UUID] = uuid4()
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: Optional[UUID] = uuid4()
    is_active: bool
    items: list[Item] = []

    # class Config:
    #     orm_mode = True


class OrderBase(BaseModel):
    isin: str
    quantity: int
    price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: Optional[UUID] = uuid4()


