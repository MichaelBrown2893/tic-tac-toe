from typing import TypeVar, Callable
from typeguard import typechecked
import inspect

T = TypeVar('T')


@typechecked
def _get_string(prompt: str = "Input: ") -> str:
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
def _cast_value(value: str, return_type: T) -> T:
    """Casts str input to given type

    Parameters
    ----------
    value
        Value to be converted to given type

    return_type
        Expected type to convert value to

    Raises
    ------
    TypeError
        Value cannot be cast to type return_type

    ValueError
        Value cannot be cast to type return_type

    BaseException
        Error raised when trying to cast value to return_type

    Returns
    -------
    T
        value cast to return_type
    """
    try:
        return return_type(value)
    except TypeError:
        raise TypeError(f"Input '{value}' cannot be cast to type {return_type}.")
    except ValueError:
        raise ValueError(f"Input '{value}' cannot be cast to type {return_type}.")
    except BaseException as err:
        raise err


@typechecked
def _check_condition(value: str, condition: Callable) -> bool:
    """Checks the value against the condition.

    Returns true is value meets condition
    Returns false if value does not meet condition

    Parameters
    ----------
    value
        The value to check

    condition
        The boolean function to check the value against

    Raises
    ------
    BaseException
        Exception raised when calling condition with value

    Returns
    -------
    bool
        If value meets condition returns true. If not returns false
    """
    try:
        return condition(value)
    except BaseException as err:
        raise Exception(f"{err}")


@typechecked
def get_input(prompt: str = "Input: ", return_type: T = str, condition: Callable = None) -> T:
    """Get input from the console

    Method can be given a specific type or condition the input must meet.
    Method will continue to prompt the user until type and condition are met.

    Parameters
    ----------
    prompt
        Text prompt to present to the user when requesting input

    return_type
        Expected return type from this method. Method will attempt to cast input to this type

    condition
        Boolean lambda the input must satisfy to be returned. Condition must be given as lambda

    Raises
    ------
    BaseException
         Exception other than ValueError or TypeError raised failed Casting

    """
    value = _get_string(prompt=prompt)
    if return_type is not str:
        try:
            value = _cast_value(value=value,return_type=return_type)
        except TypeError as err:
            print(f"{err}")
            return get_input(prompt=prompt, return_type=return_type, condition=condition)
        except ValueError as err:
            print(f"{err}")
            return get_input(prompt=prompt, return_type=return_type, condition=condition)
        except BaseException as err:
            raise err

    if condition is not None:
        if not condition(value):
            print(
                f"Input: '{value}' did not meet condition: {inspect.getsource(condition)[inspect.getsource(condition).find('lambda') + 6:-3]}.")
            return get_input(prompt=prompt, return_type=return_type, condition=condition)

    return value


@typechecked
def get_yes_or_no(prompt: str = "Enter 'y' or 'n': ") -> bool:
    """Get a boolean response from console input

    Parameters
    ----------
    prompt
        Text prompt to be displayed to the user when requesting input
    """
    return get_input(prompt=prompt, condition=lambda x: x == 'y' or x == 'n').lower() == 'y'
