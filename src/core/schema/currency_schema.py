from pydantic import BaseModel



class Result(BaseModel):
    result: float | int