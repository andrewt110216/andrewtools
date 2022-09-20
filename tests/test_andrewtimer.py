import pytest
import time
import re
from andrewtools import AndrewTimer

# Fixtures
@pytest.fixture
def t():
    return AndrewTimer()

# Tests
def test_init(t):
    assert t.laps == []
    assert time.time() - t.start_time < 0.01

# units: minutes
def test_elapsed_m(t):
    time.sleep(0.1)
    elapsed = t.elapsed(units='m')
    assert 0.001 < elapsed < 0.002
    assert type(elapsed) == float
    elapsed = t.elapsed(units='m', format=True)
    assert type(elapsed) == str
    assert re.search(r"0.00\dm", elapsed)

# units: seconds
def test_elapsed_s(t):
    time.sleep(0.1)
    elapsed = t.elapsed()
    assert 0.1 < elapsed < 0.11
    assert type(elapsed) == float
    elapsed = t.elapsed(units='s', format=True)
    assert type(elapsed) == str
    assert re.search(r"0.1\d\ds", elapsed)

# units: milliseconds
def test_elapsed_ms(t):
    time.sleep(0.1)
    elapsed = t.elapsed(units='ms')
    assert 100 < elapsed < 110
    assert type(elapsed) == float
    elapsed = t.elapsed(units='ms', format=True)
    assert type(elapsed) == str
    assert re.search(r"10\d.\d\d\dms", elapsed)

# units: nanoseconds
def test_elapsed_ms(t):
    time.sleep(0.1)
    elapsed = t.elapsed(units='ns')
    assert 100_000 < elapsed < 110_000
    assert type(elapsed) == float
    elapsed = t.elapsed(units='ns', format=True)
    assert type(elapsed) == str
    assert re.search(r"10\d,\d\d\d.\d\d\dns", elapsed)

# Laps
def test_lap():
    t = AndrewTimer()
    for _ in range(10):
        time.sleep(0.03)
        t.lap()
    assert len(t.get_laps()) == 10
    assert 0.3 < t.elapsed() < 0.4
    assert 0.03 < t.average() < 0.04
    assert 0.03 < t.last_lap() < 0.04
    assert 30 < t.average('ms') < 40
    assert 30_000 < t.average('ns') < 40_000
    assert re.search(r"0.00\dm", t.average('m', format=True))
    assert re.search(r"0.00\dm", t.last_lap('m', format=True))
    assert re.search(r"[34]\d.\d{3}ms", t.average('ms', format=True))
    laps = t.get_laps()
    for lap in laps:
        assert 0.03 < lap < 0.04
