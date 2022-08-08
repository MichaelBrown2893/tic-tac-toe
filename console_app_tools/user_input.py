from typing import overload, TypeVar, Generic
from functools import singledispatch

T = TypeVar('T')


def get_input(prompt: str = "Input: ") -> str:
    """Get str input from console"""
    return input(prompt)


def get_input_of_type(input_type: T, prompt: str = "Input: ") -> T:
    """Gets input of type from console"""
    try:
        return input_type(get_input(prompt=prompt))
    except ValueError as err:
        raise ValueError(f"{type(err)}: raised when converting console input to {input_type}: {err}")
    except Exception as err:
        raise err
