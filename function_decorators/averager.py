class Averager():
    """A class to calculate a running average. It creates instances that are callable."""
    
    def __init__(self):
        self.series = []

    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


if __name__=='__main__':
    avg = Averager()
    print('avg(10): ', avg(10))
    print('avg(11): ', avg(11))
    print('avg(12): ', avg(12))
