
import time
import signal

def test(i):
    time.sleep(i%4)
    print "%d within time"%(i)
    return i

if __name__ == '__main__':
    def handler(signum, frame):
        raise AssertionError

    i = 0
    for i in range(1, 10):
        try:
            signal.signal(signal.SIG_IGN, handler)
            signal.SIGINT
            test(i)
            i = i + 1
            signal.alarm(0)
        except AssertionError:
            print "%d timeout"%(i)