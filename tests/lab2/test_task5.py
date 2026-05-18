import threading
from src.lab2.task5 import increase
import src.lab2.task5 as task5


def run_threads():
    task5.count = 0
    threads = [threading.Thread(target=increase) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return task5.count


def test_race_inf():
    res = [run_threads() for _ in range(5)]
    assert any(r != 10000 for r in res)





