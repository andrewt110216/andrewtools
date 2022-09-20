import pytest
import re
from andrewtools import progress_bar
from andrewtools import AndrewTimer


def test_main(capfd):
    total = 10
    for iteration in range(total):
        percent = (iteration + 1) / total * 100
        bar = "*" * (iteration + 1) + "-" * (total - iteration - 1)
        expected = f"\rProgress |{bar}| {percent:.1f}% \r"
        if iteration == total - 1:
            expected += "\n"
        progress_bar(iteration, total, width=10, label="Progress")
        out, err = capfd.readouterr()
        assert expected == out

def test_main_with_end(capfd):
    total = 10
    t = AndrewTimer()
    for iteration in range(total):
        percent = (iteration + 1) / total * 100
        bar = "*" * (iteration + 1) + "-" * (total - iteration - 1)
        end = t.elapsed('s', True)
        expected = f"\rProgress |{bar}| {percent:.1f}% {end}\r"
        if iteration == total - 1:
            expected += "\n"
        progress_bar(iteration, total, width=10, label="Progress", end=end)
        out, err = capfd.readouterr()
        assert expected == out

def test_user_error_iteration_too_large(capfd):
    total = 10
    for iteration in range(total):
        # user mistakenly allows iteration to become greater than total
        progress_bar(iteration + 2, total, width=10, label="Progress")
        out, err = capfd.readouterr()
        # check for error message when `iteration` >= total
        if (iteration + 2) >= total:
            assert "Progress Bar error: iteration > total" in out
        # make sure we never print a % larger than 100%
        match = re.search(r"(\d+.\d)%", out)
        if match and (g := match.groups()):
            percent = float(g[0])
            if iteration + 2 == total - 1:
                assert percent == 100
            else:
                assert percent <= 100

def test_invalid_argument_type():
    with pytest.raises(Exception) as e:
        iterations = 10
        for i in range(iterations):
            progress_bar("Progress", i, iterations, 10)
            pass
    assert e.type == ValueError or e.type == TypeError

def test_invalid_width_values():
    # width too large
    with pytest.raises(ValueError) as e:
        progress_bar(0, 10, width=101)
    assert "width must be an integer between 10 and 100" in str(e.value)
    # width too small
    with pytest.raises(ValueError) as e:
        progress_bar(0, 10, width=9)
    assert "width must be an integer between 10 and 100" in str(e.value)
