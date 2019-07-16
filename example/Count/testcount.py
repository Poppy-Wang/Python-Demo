from count import Count
class Testcount:
    def test_add(self):
        j=Count(2,4)
        result=add=j.add()
        print(result)
mytest=Testcount()
mytest.test_add()