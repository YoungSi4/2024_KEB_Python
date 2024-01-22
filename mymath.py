def isprime(n) -> bool: # 리턴값 명시. 없어도 되는데 있으면 더 좋다.
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 반환
    :param n: 소수인지 판정할 매개변수
    :return: 소수 True, 아니면 False
    """
    pass
    if n < 2:
        return False # False를 반환하고 함수를 즉시 종료한다.

    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True # True를 반환하고 함수를 즉시 종료한다.