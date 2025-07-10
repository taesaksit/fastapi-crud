from pydantic import BaseModel

class BookBase(BaseModel):
    title : str
    price: float
    
class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id:int
    class config:
        orm_mode = True