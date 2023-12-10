class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value <= self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False

class QueryBuilder:
    def __init__(self):
        self._conditions = []

    def playsIn(self, team):
        self._conditions.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._conditions.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._conditions.append(HasFewerThan(value, attr))
        return self

    def oneOf(self, *matchers):
        return Or(*matchers)

    def build(self):
        return And(*self._conditions)