from typing import TypeVar, Callable
from typeguard import typechecked
import inspect

T = TypeVar('T')


def get_input_new(prompt: str = "Input: ", return_type: T = str, condition: Callable = None) -> T:
    value = input(prompt)
    if return_type is not str:
        try:
            value = return_type(value)
        except TypeError:
            print(f"Input '{value}' cannot be cast to type {return_type}.")
            return get_input_new(prompt=prompt, return_type=return_type, condition=condition)
        except ValueError:
            print(f"Input '{value}' cannot be cast to type {return_type}.")
            return get_input_new(prompt=prompt, return_type=return_type, condition=condition)
        except BaseException as err:
            raise err

    if condition is not None:
        if not condition(value):
            print(
                f"Input: '{value}' did not meet condition: {inspect.getsource(condition)[inspect.getsource(condition).find('lambda x:') + 9:-3]}.")
            return get_input_new(prompt=prompt, return_type=return_type, condition=condition)

    return value


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


@typechecked
def get_input_of_type_forced(input_type: T, prompt: str = "Input: ") -> T:
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
        print(f"{type(err)}: raised when converting console input to {input_type}: {err}")
        return get_input_of_type_forced(input_type, prompt)
    except Exception as err:
        raise err


def get_yes_or_no(prompt: str = "Enter 'y' or 'n': ") -> bool:
    return get_input_with_condition(prompt, lambda x: x == 'y' or x == 'n').lower() == 'y'


def get_input_with_condition(prompt: str, condition: Callable) -> str:
    while True:
        value = get_input(prompt)
        if condition(value):
            return value
        print(
            f"Input: {value} did not meet condition: {inspect.getsource(condition)[inspect.getsource(condition).find('lambda x:') + 9:-3]}.")


def get_input_of_type_with_condition(input_type: T, prompt: str, condition: Callable) -> T:
    while True:
        value = get_input_of_type_forced(input_type, prompt)
        if condition(value):
            return value
        print(
            f"Input: {value} did not meet condition: {inspect.getsource(condition)[inspect.getsource(condition).find('lambda x:') + 9:-3]}.")
