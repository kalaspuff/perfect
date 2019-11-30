import perfect


def test_class_methods():
    class X:
        called = 0

        @classmethod
        def clsmethod(cls, id_=0):
            def _fn(id_=0):
                cls.called += 1
                return id_

            return perfect.decorator(1, 2, 3, 4)(_fn)(id_=id_)

        @perfect
        @classmethod
        def classicclassmethod(cls, id_=0):
            def _fn(id_=0):
                cls.called += 1
                return id_

            return _fn(id_=id_)

        @perfect(value="yes")
        def func(self, id_=0):
            @perfect
            def _fn(id_=0):
                return id_

            return _fn(id_=id_)

        @staticmethod
        def stat(*args, **kwargs):
            kw_value = kwargs.get("id_", None)
            if kw_value is None and args:
                return args[0]
            return kw_value

        @perfect.decorator
        @staticmethod
        def dstat(*args, **kwargs):
            kw_value = kwargs.get("type_", None)
            if kw_value is None and args:
                return args[0]
            return kw_value

    @perfect(id=4711, id_=1338, type_=0)
    def local_func(id_, type_):
        return id_ * type_

    assert X.clsmethod(id_=20) == 20
    assert X().clsmethod(id_=19) == 19
    assert perfect(X.clsmethod)(id_=18) == 18
    assert perfect(X.clsmethod)(17) == 17
    assert perfect.decorator(X().clsmethod)(16) == 16

    assert X.called == 5

    assert X().func(id_=15) == 15
    assert X().func(14) == 14

    assert X.stat(id_=13) == 13
    assert X().stat(id_=12) == 12
    assert perfect(X.stat)(id_=11) == 11
    assert perfect(X().stat)(10) == 10

    assert X.dstat(9) == 9
    assert X().dstat(8) == 8
    assert X.dstat(type_=7) == 7
    assert X().dstat(type_=6) == 6

    assert local_func(**{"id_": 13, "type_": 7}) - 86 == 5
    assert local_func(13, 7) - 87 == 4
    assert local_func(type_=7, **{"id_": 13}) - 88 == 3

    assert X.classicclassmethod(id_=2) == 2
    assert X().classicclassmethod(id_=1) == 1

    assert X.called == 7

    assert X.classicclassmethod() == 0
    assert X().classicclassmethod(-1) == -1

    assert X.called == 9
