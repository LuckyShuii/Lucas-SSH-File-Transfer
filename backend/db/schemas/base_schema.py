from typing import ForwardRef, Union
from sqlalchemy_pydantic_orm import ORMBaseSchema

REFS = {}

class BaseSchema(ORMBaseSchema):
    def __init_subclass__(cls) -> None:
        if cls.__name__ not in REFS:
            REFS[cls.__name__] = cls
        return super().__init_subclass__()

    @staticmethod
    def forward_all():
        for _, cls in REFS.items():
            cls_refs = {}
            for field in cls.__fields__:
                annotation_type = get_inner(cls.__fields__[field].type_)
                if type(annotation_type) == str:
                    if annotation_type in REFS:
                        cls_refs[annotation_type] = REFS[annotation_type]
                    else:
                        print("Can't find reference for", annotation_type)
            if cls_refs:
                cls.update_forward_refs(**cls_refs)

def get_inner(annotation):
    is_list = hasattr(annotation, "__origin__") and annotation.__origin__ == list
    is_optional = hasattr(annotation, "__origin__") and annotation.__origin__ == Union
    is_forward = isinstance(annotation, ForwardRef)

    if is_list or is_optional:
        return get_inner(annotation.__args__[0])
    if is_forward:
        return get_inner(annotation.__forward_arg__)
    return annotation