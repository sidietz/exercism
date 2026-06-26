"""
implements HighScores
"""

class HighScores:
    """
    implements HighScores
    """
    def __init__(self, scores):
        new_scores = scores[:]
        new_scores.sort()
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        new_scores = self.scores[:]
        new_scores.sort()
        return new_scores[-1]

    def personal_top_three(self):
        new_scores = self.scores[:]
        new_scores.sort()
        return new_scores[::-1][0:3]
        

