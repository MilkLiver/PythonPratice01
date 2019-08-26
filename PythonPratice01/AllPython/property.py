class Exam(object):
    score=87
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        print('test')
        return None
        #return self._score

    @score.setter
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val
            
e=Exam(60)
print(e.score)
e.score=66
print(e.score)
