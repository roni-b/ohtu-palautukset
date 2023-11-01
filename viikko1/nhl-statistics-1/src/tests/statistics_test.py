import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
  def setUp(self):
    self.stats = StatisticsService(
       PlayerReaderStub()
    )

  def test_search_found(self):
     result = self.stats.search("Kurri")
     self.assertEqual(result.name, "Kurri")

  def test_search_not_found(self):
     result = self.stats.search("asd")
     self.assertIsNone(result)

  def test_team(self):
     result = self.stats.team("PIT")
     self.assertIsNotNone(result)

  def test_top_returns_players(self):
     result = self.stats.top(3)
     self.assertEqual(len(result), 4)
