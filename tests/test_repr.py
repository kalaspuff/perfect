import perfect
from perfect import decorator


def test_repr():
    id_ = hex(id(perfect))
    assert str(perfect) == f"<perfect.decorator object at {id_}>"
    assert str(perfect.decorator) != f"<perfect.decorator object at {id_}>"
    assert str(decorator) == str(perfect.decorator)

    assert repr(perfect) == f"<perfect.decorator object at {id_}>"
    assert repr(perfect.decorator) != f"<perfect.decorator object at {id_}>"
    assert repr(decorator) == repr(perfect.decorator)

    assert perfect is not perfect.decorator
    assert perfect is not decorator
    assert perfect.decorator is decorator

    assert str(perfect()) != f"<perfect.decorator object at {id_}>"
    assert str(perfect.decorator()) != f"<perfect.decorator object at {id_}>"
    assert str(decorator()) != f"<perfect.decorator object at {id_}>"

    assert repr(perfect()) != f"<perfect.decorator object at {id_}>"
    assert repr(perfect.decorator()) != f"<perfect.decorator object at {id_}>"
    assert repr(decorator()) != f"<perfect.decorator object at {id_}>"

    assert str(perfect()).startswith("<perfect.decorator object at")
    assert str(perfect.decorator()).startswith("<perfect.decorator object at")
    assert str(decorator()).startswith("<perfect.decorator object at")

    assert repr(perfect()).startswith("<perfect.decorator object at")
    assert repr(perfect.decorator()).startswith("<perfect.decorator object at")
    assert repr(decorator()).startswith("<perfect.decorator object at")

    assert str(perfect()) != str(perfect)
    assert str(perfect()) != str(perfect())
    assert str(perfect()) != str(perfect.decorator())
    assert str(perfect()) != str(decorator())


def test_wrapped_repr():
    id_ = hex(id(perfect))
    assert str(perfect) == f"<perfect.decorator object at {id_}>"
    assert str(perfect.decorator) != f"<perfect.decorator object at {id_}>"
    assert str(decorator) == str(perfect.decorator)

    def wrapped_func():
        pass

    func_id = hex(id(wrapped_func))
    func = perfect(wrapped_func)

    start_str = "function test_wrapped_repr.<locals>.wrapped_func at"

    assert str(func) != f"<{start_str} {id_}>"
    assert str(func) == f"<{start_str} {func_id}>"
    assert repr(func) != f"<{start_str} {id_}>"
    assert repr(func) == f"<{start_str} {func_id}>"

    func = perfect(4711, 1338, a=1, b=2, **{"id": 55})(wrapped_func)
    assert str(func) != f"<{start_str} {id_}>"
    assert str(func) == f"<{start_str} {func_id}>"
    assert repr(func) != f"<{start_str} {id_}>"
    assert repr(func) == f"<{start_str} {func_id}>"

    func = perfect.decorator(wrapped_func)
    assert str(func) != f"<{start_str} {id_}>"
    assert str(func) == f"<{start_str} {func_id}>"
    assert repr(func) != f"<{start_str} {id_}>"
    assert repr(func) == f"<{start_str} {func_id}>"

    func = perfect.decorator()(wrapped_func)
    assert str(func) != f"<{start_str} {id_}>"
    assert str(func) == f"<{start_str} {func_id}>"
    assert repr(func) != f"<{start_str} {id_}>"
    assert repr(func) == f"<{start_str} {func_id}>"
