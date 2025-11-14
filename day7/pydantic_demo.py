"""
pydantic
运行时验证
BaseModel

"""
from dataclasses import dataclass
from typing import Optional
import json
from pydantic import BaseModel, Field, field_validator


class Person(BaseModel):
    name: str
    # Field(frozen=True) 设置为不可变 类似final;还有le和ge等
    age: int = Field(frozen=True, le=99)
    # 通过Optional赋默认值
    address: Optional[str] = None
    phone: list[str] = []

    # 默认先走Field 再走 field_validator 当然可以通过参数调整
    @field_validator('phone')
    @classmethod
    def validate_phones(cls, param: list[str]) -> list[str]:
        for v in param:
            if len(v) != 11 or v[0] != '1':
                raise ValueError(f'Invalid phone number: {v}')
        return param

# 支持多次校验 也就是返回每个校验器的结果
p = Person(name='wang', age=99, phone=['12222222222', '13199998888'])


p2_dict = {"name": 'li', "age": 22}
# 使用python自带的解构生成对象
# p2 = Person(**p2_dict)


p2_json = json.dumps(p2_dict)
# 使用pydantic直接从json转为BaseModel
p2 = Person.model_validate_json(p2_json)
print(p2)

s = p2.model_dump_json()
print(s)

print(p)

# @dataclass
# 装饰器
# 自动生成 __init__ 方法，从而无需手动编写初始化代码。
# 自动生成 __repr__ 方法，提供对象的字符串表示。
# 自动生成 __eq__ 方法，用于比较两个实例是否相等。
# 可以根据需要生成 __hash__ 方法。
# 支持默认值和类型注解，使得代码更加清晰。
# class Student(Person):
#     name: str
#     gender: str
#
# s = Student(name='李四', gender='女')
# print(s)
