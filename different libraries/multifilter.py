class multifilter:
    def judge_half(pos, neg):
        return pos >= neg   # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1     # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0     # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable    # iterable - исходная последовательность
        self.funcs = funcs          # funcs - допускающие функции
                                    # judge - решающая функция

    def __iter__(self):
        yield elem   # возвращает итератор по результирующей последовательности