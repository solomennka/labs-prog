import threading
from src.lab2.task6 import increase
import src.lab2.task6 as task6


def run_threads():
    task6.count = 0
    threads = [threading.Thread(target=increase) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return task6.count


def test_race_inf():
    res = [run_threads() for _ in range(5)]
    print(res)
    assert all(r == 1000 for r in res)





