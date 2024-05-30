from fastapi import HTTPException


def is_valid_enum(value, class_enum):
    try:
        class_enum(value)
    except ValueError:
        raise HTTPException(status_code=404, detail="Status Value Error")
