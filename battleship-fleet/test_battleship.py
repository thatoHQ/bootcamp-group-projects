import unittest
import battleship


class TestBattleshipShots(unittest.TestCase):
    def test_legal_shots_exclude_already_fired_cells(self):
        state = battleship.parse_state("destroyer:A1,A2 | A1,B7")
        legal = battleship.generate_legal_shots(state)
        self.assertNotIn("A1", legal)
        self.assertNotIn("B7", legal)
        self.assertIn("C3", legal)

    def test_apply_shot_hit_not_yet_sunk(self):
        state = battleship.parse_state("destroyer:A1,A2 | B7")
        result = battleship.apply_shot(state, "A1")
        self.assertEqual(result["result"], "hit")

    def test_apply_shot_miss(self):
        state = battleship.parse_state("destroyer:A1,A2 | B7")
        result = battleship.apply_shot(state, "C3")
        self.assertEqual(result["result"], "miss")

    def test_apply_shot_sinks_ship(self):
        state = battleship.parse_state("destroyer:A1,A2 | A1")
        result = battleship.apply_shot(state, "A2")
        self.assertEqual(result["result"], "sunk:destroyer")

    def test_cannot_fire_at_same_cell_twice(self):
        state = battleship.parse_state("destroyer:A1,A2 | A1")
        with self.assertRaises(ValueError):
            battleship.apply_shot(state, "A1")

    def test_fleet_defeated_when_all_ships_sunk(self):
        state = battleship.parse_state("destroyer:A1,A2 | A1")
        result = battleship.apply_shot(state, "A2")
        self.assertTrue(result["fleet_defeated"])


if __name__ == "__main__":
    unittest.main()