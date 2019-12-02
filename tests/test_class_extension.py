import pytest

import perfect


def test_class_extension():
    assert perfect.__version__

    class testdecorator(perfect):
        __author__ = "Test"

        def _test(self, value):
            return value

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

    d = testdecorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5

    d = testdecorator.decorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5

    class anotherdecorator(testdecorator):
        def _other_test(self, value):
            return value * 2

    assert anotherdecorator.__author__

    assert anotherdecorator.decorator
    assert anotherdecorator.decorator()

    assert anotherdecorator._test
    with pytest.raises(TypeError):
        anotherdecorator._test()

    with pytest.raises(TypeError):
        anotherdecorator._test(5)

    d = anotherdecorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5
    assert d._other_test(5) == 10

    d = anotherdecorator.decorator()
    assert d._test
    with pytest.raises(TypeError):
        d._test()
    assert d._test(5) == 5
    assert d._other_test(5) == 10
