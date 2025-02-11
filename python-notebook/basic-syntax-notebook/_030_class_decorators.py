# You can have class decorators too

class Counter:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'Counter: {self.count}')
        return self.func(*args, **kwargs)

@Counter
def retry(name):
    print(f'Executing again {name}')


retry('Binary Search')
retry('Binary Search')
retry('Binary Search')
retry('Binary Search')
