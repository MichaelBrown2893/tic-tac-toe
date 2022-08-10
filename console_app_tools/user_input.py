from typing import overload, TypeVar, Generic
from functools import singledispatch

from typeguard import typechecked

T = TypeVar('T')


@typechecked
def get_input(prompt: str = "Input: ") -> str:
    """Get str input from console

    Parameters
    ----------
    prompt
        The text information to be given to the user when requesting input

    Returns
    -------
    str
        Text input by the user
    """
    return input(prompt)


@typechecked
def get_input_of_type(input_type: T, prompt: str = "Input: ") -> T:
    """Gets input of type from console

    Parameters
    ----------
    input_type
        The type to convert the users input into
    prompt
        The text information to be given to the user when requesting input

    Raises
    ------
    ValueError
        Failed to cast input to the given type
    Exception
        Error raised while getting input

    Returns
    -------
    T
        Returns the users input in the type given in input_type
    """
    try:
        return input_type(get_input(prompt=prompt))
    except ValueError as err:
        raise ValueError(f"{type(err)}: raised when converting console input to {input_type}: {err}")
    except Exception as err:
        raise err
