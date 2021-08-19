import pickle as pkl

class MyClass():
    def __init__(self, num) -> None:
        self.num = num
    def __str__(self):
        return 'my num: %s' % self.num

with open('pkl_file.pkl', 'wb') as f:
    pkl.dump(MyClass(5942), f)

with open('pkl_file.pkl', 'rb') as f:
    # for i in range(5):
    print(pkl.load(f))