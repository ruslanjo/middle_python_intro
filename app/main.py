"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Return the greeting text.

    Args:
        name (str): Name from an input.

    Returns:
        str: The name after capitalizing and concatenation with greeting text.

    """
    return 'Привет, {capitalized_name}'.format(capitalized_name=name.title())
