import timeit


def test_string_concatenation():
    # 작은 크기의 문자열을 여러 번 반복하여 연결
    small_string = "a" * 100
    repetitions = 100_000

    # 문자열 연결 방식 1: 반복문을 통한 문자열 연결
    def concat_with_loop():
        result = ""
        for _ in range(repetitions):
            result += small_string
        return result

    # 문자열 연결 방식 2: join() 메서드를 사용한 문자열 연결
    def concat_with_join():
        result = []
        for _ in range(repetitions):
            result.append(small_string)
        return ''.join(result)

    # 문자열 연결 방식 3: 리스트 컴프리헨션과 join() 메서드를 사용한 문자열 연결
    def concat_with_comprehension():
        result = ''.join([small_string for _ in range(repetitions)])
        return result

    # 문자열 연결 방식 4: join() 메서드를 사용한 문자열 연결 (리스트 생성 없이)
    def concat_with_join_no_list():
        result = ''.join(small_string for _ in range(repetitions))
        return result

    # 각 방식별 실행 시간 측정
    time_loop = timeit.timeit(concat_with_loop, number=1)
    time_join = timeit.timeit(concat_with_join, number=1)
    time_comprehension = timeit.timeit(concat_with_comprehension, number=1)
    time_join_no_list = timeit.timeit(concat_with_join_no_list, number=1)

    # 결과 출력
    print(f"Concatenation with loop: {time_loop} seconds")
    print(f"Concatenation with join: {time_join} seconds")
    print(f"Concatenation with comprehension: {time_comprehension} seconds")
    print(f"Concatenation with join (no list): {time_join_no_list} seconds")


# 테스트 실행
test_string_concatenation()
