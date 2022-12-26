from typing import Optional

from schemas import CamelModel


class usersSchema(CamelModel):
    email: str
    password: str


class CreateBrandSchema(CamelModel):
    enter_brand_competitor_hashtag: str
    email: Optional[str] = None
