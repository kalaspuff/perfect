import pytest

import perfect
from perfect import decorator


@pytest.mark.parametrize("value", [perfect, decorator, perfect.decorator, perfect(), decorator(), perfect.decorator()])
def test_wrapper(value):
    func = value(lambda x: x)
    assert func("input_data") == "input_data"


@pytest.mark.parametrize("value", [perfect, decorator, perfect.decorator, perfect(), decorator(), perfect.decorator()])
def test_wrapped_class_func(value):
    class X:
        def func(self, data=0):
            return data

    assert value(X().func)(4711) == 4711
    assert value(X().func)() == 0
    assert value(X().func)(data=1337) == 1337
    assert value(X().func)(data=1338) == 1338
    assert value(X().func)(**{"data": -5050}) == -5050
    assert value(X().func)(**{"data": 999999}) == 999999


@pytest.mark.parametrize("value", [perfect, decorator, perfect.decorator, perfect(), decorator(), perfect.decorator()])
def test_decorated_class_func(value):
    class X:
        @value
        def func(self, data=0):
            return data

        def non_decorated_func(self, data=0):
            return data

    assert X().func(4711) == 4711
    assert X().func() == 0
    assert X().func(data=1337) == 1337
    assert X().func(data=1338) == 1338
    assert X().func(**{"data": -5050}) == -5050
    assert X().func(**{"data": 999999}) == 999999

    x = X()
    assert x.func(4711) == 4711
    assert x.func() == 0
    assert x.func(data=1337) == 1337
    assert x.func(data=1338) == 1338
    assert x.func(**{"data": -5050}) == -5050
    assert x.func(**{"data": 999999}) == 999999

    assert x.non_decorated_func(**{"data": 999999}) == 999999
    with pytest.raises(TypeError):
        x.non_decorated_func(**{"data": 999999, "extra_key": True})


@pytest.mark.parametrize("value", [perfect, decorator, perfect.decorator, perfect(), decorator(), perfect.decorator()])
def test_failed_kwargs(value):
    func = lambda data=None: "42"  # noqa
    assert func(None) == "42"
    assert func(data=1338) == "42"
    with pytest.raises(TypeError):
        assert func(data_=1338) == "42"
    assert func(**{"data": 4711}) == "42"
    with pytest.raises(TypeError):
        assert func(**{"data_": 4711}) == "42"

    def _func(data=None):
        return "42"

    func = _func
    assert func(None) == "42"
    with pytest.raises(TypeError):
        assert func(data_=1338) == "42"
    assert func(data=1338) == "42"
    with pytest.raises(TypeError):
        assert func(**{"data_": 4711}) == "42"
    assert func(**{"data": 4711}) == "42"

    func = _func
    assert func(None) == "42"
    with pytest.raises(TypeError):
        assert func(data=1338, extra=True) == "42"
    assert func(data=1338) == "42"
    with pytest.raises(TypeError):
        assert func(**{"data": 4711, "extra": False}) == "42"
    assert func(**{"data": 4711}) == "42"

    func = value(_func)
    assert func(None) == "42"
    assert func(data=1338) == "42"
    assert func(**{"data": 4711}) == "42"

    func = value(value(_func))
    assert func(None) == "42"
    assert func(data=1338) == "42"
    assert func(**{"data": 4711}) == "42"
