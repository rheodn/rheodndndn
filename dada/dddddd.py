def draw_table(data, no_classes, unit):
    # 데이터의 최솟값과 최댓값 계산
    min_val = min(data)
    max_val = max(data)

    # 클래스 범위 계산
    range_val = max_val - min_val
    class_width = (range_val / no_classes) + unit  # 클래스 폭

    # 도수 초기화
    frequencies = [0] * no_classes

    # 도수 계산
    for value in data:
        class_index = int((value - min_val) / class_width)
        if class_index >= no_classes:  # 마지막 클래스에 포함되도록 보정
            class_index = no_classes - 1
        frequencies[class_index] += 1

    # 도수분포표 출력
    print("도수분포표:")
    print("구간\t도수")
    for i in range(no_classes):
        lower_bound = min_val + i * class_width
        upper_bound = lower_bound + class_width
        print(f"{lower_bound:.2f} ~ {upper_bound:.2f}\t{frequencies[i]}")


def draw_histogram(data, no_classes, unit):
    # 데이터의 최솟값과 최댓값 계산
    min_val = min(data)
    max_val = max(data)

    # 클래스 범위 계산
    range_val = max_val - min_val
    class_width = (range_val / no_classes) + unit  # 클래스 폭

    # 도수 초기화
    frequencies = [0] * no_classes

    # 도수 계산
    for value in data:
        class_index = int((value - min_val) / class_width)
        if class_index >= no_classes:  # 마지막 클래스에 포함되도록 보정
            class_index = no_classes - 1
        frequencies[class_index] += 1

    # 상대도수 계산
    total_count = sum(frequencies)
    relative_frequencies = [freq / total_count for freq in frequencies]

    # 히스토그램 출력
    print("\n상대도수 히스토그램:")
    for i in range(no_classes):
        stars = '*' * int(relative_frequencies[i] * 100)  # 100을 곱하여 시각화
        print(f"{i + 1} 구간: {stars} ({relative_frequencies[i]:.2f})")


# 데이터와 클래스 수 설정
data = [
    41, 32, 30, 23, 24, 32, 11, 39, 24, 46,
    50, 18, 41, 14, 33, 50, 38, 25, 32, 16,
    43, 19, 35, 22, 46, 43, 10, 22, 17, 47,
    66, 48, 25, 43, 28, 31, 12, 25, 12, 48,
    41, 32, 30, 23, 24, 32, 11, 9, 24, 46,
    50, 18, 41, 14, 33, 50, 38, 25, 32, 16,
    43, 19, 35, 22, 46, 43, 10, 22, 17, 47,
    66, 48, 25, 43, 28, 31, 12, 25, 12, 48
]
no_classes = 6
unit = 1

# 함수 호출
draw_table(data, no_classes, unit)
draw_histogram(data, no_classes, unit)
