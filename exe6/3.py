# 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})


class dictclass(object):

    def __init__(self, dic):
        self.dic = dic

    def del_dict(self, key):
        del self.dic['a']

    def get_dict(self, key):
        if key in self.dic:
            res = self.dic[key]
        else:
            res = 'not found'
        return res

    def get_key(self):
        list = []
        for key in self.dic.keys():
            list.append(key)
        return list

    def update_dict(self, dic2):
        list = []
        for key, values in dic2.items():
            if key in self.dic:
                self.dic[key] += values
            else:
                self.dic[key] = values
        for values in self.dic.values():
            list.append(values)
        return list


dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic2 = {'a': 6, 'e': 5}
d = dictclass(dict_)
d.del_dict('a')
print(dict_)
print(d.get_dict('c'))
print(d.get_key())
print(d.update_dict(dic2))
