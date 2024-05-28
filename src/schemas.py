from typing import Union, List, Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from uuid import UUID, uuid4


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: Optional[UUID] = uuid4()

    # model_config = ConfigDict(
    #     arbitrary_types_allowed=True,
    #     from_attributes=True
    # )


class OrderBase(BaseModel):
    isin: str
    quantity: int
    price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: Optional[UUID] = uuid4()


