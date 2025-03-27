import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """이 함수는 2D 리스트와 start, end 인덱스를 받아서 슬라이싱을 합니다.
    Args:
        family (list): 2D 리스트입니다.
        start (int): 시작 인덱스입니다.
        end (int): 끝 인덱스입니다.
    Returns:
        list: 슬라이싱된 2D 리스트입니다.
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list, start and end must be integer")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("family must be a list, start and end must be integer")
    if start >= len(family) or end >= len(family):
        raise ValueError("start and end must be less")
    x = slice(start, end)
    print("My shape is :", np.array(family).shape)
    print("My new shape is :", np.array(family)[x].shape)
    return np.array(family)[x].tolist()
