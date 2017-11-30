print('This is executed')


class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass

ml = MyList([1, 10, 15, 2, 7])
ml.sort()
print(ml)
