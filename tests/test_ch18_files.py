from pathlib import Path
import tempfile
from ch18_files import average_by_team, copy_matching, longest_line, sum_file, top_words, write_report


def test_ex_18_1():
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        (tmp / "n.txt").write_text("3\n\n-1\n10\n")
        (tmp / "empty.txt").write_text("")
        assert sum_file(tmp / "n.txt") == 12 and sum_file(tmp / "empty.txt") == 0


def test_ex_18_2():
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        (tmp / "w.txt").write_text("The cat and the hat.\nThe end, and THE start!\n")
        assert top_words(tmp / "w.txt", 2) == [("the", 4), ("and", 2)]
        assert top_words(tmp / "w.txt", 4) == [("the", 4), ("and", 2), ("cat", 1), ("end", 1)] and len(top_words(tmp / "w.txt", 99)) == 6


def test_ex_18_3():
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        path = tmp / "report.csv"
        path.write_text("old contents\n")
        assert write_report(path, {"ana": 7, "bo": 9, "cy": 7}) == 3 and path.read_text() == "bo,9\nana,7\ncy,7\n"
        assert write_report(path, {}) == 0 and path.read_text() == ""


def test_ex_18_4():
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        (tmp / "a.txt").write_text("ab\nabcd\n\n")
        with open(tmp / "big.txt", "w") as f:
            for i in range(100_000):
                f.write("x" * (i % 97) + "\n")
            f.write("y" * 500)
        assert longest_line(tmp / "a.txt") == 4 and longest_line(tmp / "big.txt") == 500


def test_ex_18_5():
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        (tmp / "log.txt").write_text("error: disk\nok\nerror: net")
        assert copy_matching(tmp / "log.txt", tmp / "out.txt", "error") == 2 and (tmp / "out.txt").read_text() == "error: disk\nerror: net"
        assert copy_matching(tmp / "log.txt", tmp / "none.txt", "panic") == 0 and (tmp / "none.txt").read_text() == ""


def test_ex_18_6():
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        (tmp / "games.csv").write_text("team,points\nred,10\nblue,4\nred,7\n")
        (tmp / "none.csv").write_text("team,points\n")
        assert average_by_team(tmp / "games.csv") == {"red": 8.5, "blue": 4.0} and average_by_team(tmp / "none.csv") == {}
        (tmp / "quoted.csv").write_text('team,points\n"red, the best",3\n')
        assert average_by_team(tmp / "quoted.csv") == {"red, the best": 3.0}
