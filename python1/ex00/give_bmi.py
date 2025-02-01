import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """ BMI 수치를 계산하는 함수입니다.  BMI = height / weight ** 2 입니다. \
        이 함수는 height와 weight를 받아서 BMI를 계산하고, 그 결과를 리턴합니다.
        Args:
            height (list[int | float]): 키 리스트입니다. 단위는 cm입니다.
            weight (list[int | float]): 몸무게 리스트입니다. 단위는 kg입니다.
        Returns:
            list[int | float]: BMI 수치 리스트입니다.
    """
    height = np.array(height)
    weight = np.array(weight)
    return (weight / height**2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ BMI 수치가 limit보다 큰지 작은지 판단하는 함수입니다. \
        이 함수는 bmi와 limit를 받아서 bmi가 limit보다 큰지 작은지 판단하고, 그 결과를 리턴합니다.
        Args:
            bmi (list[int | float]): BMI 수치 리스트입니다.
            limit (int): 비교할 값입니다.
        Returns:
            list[bool]: limit보다 크면 True, 작으면 False인 리스트입니다.
    """
    bmi = np.array(bmi)
    return (bmi > limit).tolist()
