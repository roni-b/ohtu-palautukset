class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        self.SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
        score = ""

        if self.m_score1 == self.m_score2:
            score = self._get_equal_score()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self._get_advantage_or_winner()

        else:
            score = self._get_normal_score()

        return score

    def _get_equal_score(self):
        if self.m_score1 < 3:
            return f"{self.SCORE_NAMES[self.m_score1]}-All"
        return "Deuce"

    def _get_advantage_or_winner(self):
        minus_result = self.m_score1 - self.m_score2

        if abs(minus_result) == 1:
            leader = self.player1_name if minus_result == 1 else self.player2_name
            return f"Advantage {leader}"
        else:
            leader = self.player1_name if minus_result > 1 else self.player2_name
            return f"Win for {leader}"

    def _get_normal_score(self):
        return f"{self.SCORE_NAMES[self.m_score1]}-{self.SCORE_NAMES[self.m_score2]}"