import pytest

import perfect


def test_class_extension():
    assert perfect.__version__

    class testdecorator(perfect):
        __author__ = "Test"

        def _test(self, value):
            return value

        @staticmethod
        def _staticmethod_test(value):
            return value

        @classmethod
        def _classmethod_test(cls, value):
            cls.data = value
            return (cls, value)

    with pytest.raises(AttributeError):
        testdecorator.__version__

    assert perfect.__author__
    assert testdecorator.__author__

    assert testdecorator.decorator
    assert testdecorator.decorator()

    with pytest.raises(AttributeError):
        testdecorator().decorator

    with pytest.raises(AttributeError):
        testdecorator.decorator().decorator

    assert testdecorator._test
    with pytest.raises(TypeError):
        testdecorator._test()

    with pytest.raises(TypeError):
        testdecorator._test(5)

    assert testdecorator._staticmethod_test(5) == 5
    assert testdecorator._classmethod_test(5) == (testdecorator, 5)
    assert testdecorator.data == 5

    d = testdecorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5

    assert d._staticmethod_test(5) == 5
    assert d._classmethod_test(5) == (d.__class__, 5)

    d = testdecorator.decorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5

    assert d._staticmethod_test(5) == 5
    assert d._classmethod_test(5) == (d.__class__, 5)

    class anotherdecorator(testdecorator):
        def _other_test(self, value):
            return value * 2

        @staticmethod
        def _other_staticmethod_test(value):
            return value * 2

        @classmethod
        def _other_classmethod_test(cls, value):
            return (cls, testdecorator, value * 2)

    assert anotherdecorator.__author__

    assert anotherdecorator.decorator
    assert anotherdecorator.decorator()

    assert anotherdecorator._test
    with pytest.raises(TypeError):
        anotherdecorator._test()

    with pytest.raises(TypeError):
        anotherdecorator._test(5)

    assert anotherdecorator._staticmethod_test(5) == 5
    assert anotherdecorator._classmethod_test(20) == (anotherdecorator, 20)
    assert anotherdecorator._other_staticmethod_test(5) == 10
    assert anotherdecorator._other_classmethod_test(5) == (anotherdecorator, testdecorator, 10)
    assert anotherdecorator.data == 20

    d = anotherdecorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5
    assert d._other_test(5) == 10

    assert d._staticmethod_test(5) == 5
    assert d._classmethod_test(5) == (d.__class__, 5)
    assert d._other_staticmethod_test(5) == 10
    assert d._other_classmethod_test(5) == (d.__class__, testdecorator, 10)

    d = anotherdecorator.decorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5
    assert d._other_test(5) == 10

    assert d._staticmethod_test(5) == 5
    assert d._classmethod_test(5) == (d.__class__, 5)
    assert d._other_staticmethod_test(5) == 10
    assert d._other_classmethod_test(5) == (d.__class__, testdecorator, 10)
