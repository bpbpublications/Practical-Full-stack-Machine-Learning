def get_life_details(name:str, age:int) -> str:
    # name_age = f'{name} is {age} old.'
    years_left = name + "has " + str(100-age) + " years left."
    return years_left

#print(get_life_details(name="Foo",age=35))

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    timestamp: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "name" : "foo",
    "timestamp": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)

print(user.id)
