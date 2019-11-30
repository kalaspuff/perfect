import pytest

import perfect
from perfect import decorator


def test_init():
    assert perfect
    assert perfect.decorator
    assert decorator

    assert isinstance(perfect.__version_info__, tuple)
    assert perfect.__version_info__
    assert isinstance(perfect.__version__, str)
    assert len(perfect.__version__)

    with pytest.raises(TypeError):
        "__version__" in perfect

    with pytest.raises(AttributeError):
        perfect.decorator.__version__

    with pytest.raises(AttributeError):
        decorator.__version__
