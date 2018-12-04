class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

# import copy
# 
# class FilledList(list):
#     def __init__(self, count, value, *args, **kwargs):
#         super().__init__()
#         for _ in range(count):
#             self.append(copy.copy(value))

class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)