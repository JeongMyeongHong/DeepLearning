from quiz00 import Quiz00
from domains import my100, my_random, ten_nums


class Quiz10:
    def quiz10bubble(self) -> str:
        arr = ten_nums()
        print(arr)
        for i in range(0, len(arr) - 1):
            for j in range(0, len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp
            print(f'{i}회차 배열 : {arr}')
        return None

    def quiz11insertion(self) -> str:
        arr = ten_nums()
        arr2 = []
        print(arr)
        for i in range(1, len(arr) - 1):
            for j in range(0, i):
                if arr[j] > arr[i]:
                    arr2[j] = arr[j]
                else:
                    for k in range(j, i):
                        arr


            print(f'{i}회차 배열 : {arr}')
        return None

    def quiz12selection(self) -> str:
        return None

    def quiz13quick(self) -> str:
        return None

    def quiz14merge(self) -> str:
        return None

    def quiz15magic(self) -> str:
        return None

    def quiz16zigzag(self) -> str:
        return None

    def quiz17prime(self) -> str:
        no1 = my100()
        no2 = myRandom(no1, no1 * 2)
        print(f'{no1}~{no2} 사이의 소수 출력')
        res = ''
        for i in range(no1, no2 + 1):
            for j in range(2, i + 1):
                if i == j:
                    res += f'{i} '
                elif i % j == 0:
                    break
        print(f'{res}')
        return None

    def quiz18golf(self) -> str:
        max_num = 10000
        r_num = random.randint(1, max_num)
        sel_num = max_num / 2
        left_num = 0
        right_num = max_num
        cnt = 1
        while 1:
            origin_sel_num = sel_num
            print(sel_num)
            if sel_num == r_num:
                print('정답입니다.')
                break
            elif sel_num < r_num:
                print(f'{sel_num}은 {r_num}보다 작은 숫자 입니다.')
                sel_num = int((right_num + sel_num) / 2)
                left_num = origin_sel_num
            else:
                print(f'{sel_num}은 {r_num}보다 큰 숫자 입니다.')
                sel_num = int((left_num + sel_num) / 2)
                right_num = origin_sel_num
            print(f'시도 횟수는 {cnt}번 입니다.')
            cnt += 1
        return None

    def quiz19booking(self) -> str:
        q00 = Quiz00()
        name = q00.quiz06memberChoice()

        return None
