class DivStr(str):
    def __init__(self,obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj

        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)

        if first and second:
            return DivStr(start[:-1]+finish)
        if (first and not second) or (not first and second):
            return DivStr(start+finish)
        if not first and not  second:
            return DivStr(start + '/' + finish)