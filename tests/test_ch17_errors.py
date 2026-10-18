import pytest
from ch17_errors import (ConfigError, InsufficientFunds, number_setting, parse_ages, parse_port, run_steps, use_two,
                         withdraw)


def test_ex_17_1():
    assert parse_port(" 8080 ") == 8080 and parse_port("1") == 1 and parse_port("65535") == 65535
    with pytest.raises(ValueError, match="not a number: 'http'"):
        parse_port("http")
    for bad, message in (("0", "out of range: 0"), ("70000", "out of range: 70000")):
        with pytest.raises(ValueError, match=message):
            parse_port(bad)


def test_ex_17_2():
    assert withdraw(100, 30) == 70 and withdraw(5, 5) == 0
    with pytest.raises(InsufficientFunds) as info:
        withdraw(20, 50)
    assert (info.value.needed, info.value.available) == (50, 20) and str(info.value) == "needed 50, available 20"
    assert isinstance(info.value, Exception)


def test_ex_17_3():
    assert number_setting({"port": "80"}, "port") == 80
    with pytest.raises(ConfigError) as info:
        number_setting({}, "port")
    assert isinstance(info.value.__cause__, KeyError) and str(info.value) == "setting 'port'"
    with pytest.raises(ConfigError) as info:
        number_setting({"port": "eighty"}, "port")
    assert isinstance(info.value.__cause__, ValueError)


def test_ex_17_4():
    log = []
    run_steps([lambda: log.append("a"), lambda: log.append("b")], log)
    assert log == ["start", "a", "b", "done"]

    def fail():
        raise RuntimeError("boom")

    log = []
    with pytest.raises(RuntimeError):
        run_steps([lambda: log.append("a"), fail, lambda: log.append("never")], log)
    assert log == ["start", "a", "done"]


def test_ex_17_5():
    want = ["open a", "open b", "work", "close b", "close a"]
    log = []
    use_two(log, False)
    assert log == want
    log = []
    with pytest.raises(RuntimeError):
        use_two(log, True)
    assert log == want


def test_ex_17_6():
    assert parse_ages(["34", "x", "200", " 7 "]) == ([34, 7], ["row 2: not a number: x", "row 3: out of range: 200"])
    assert parse_ages([]) == ([], []) and parse_ages(["0", "150"]) == ([0, 150], []) and parse_ages(["-1"]) == ([], ["row 1: out of range: -1"])
