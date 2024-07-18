import unittest
from unittest import mock
import io
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_id_auto(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(s2.id, s1.id + 1)

    def test_square_id_passed(self):
        s = Square(1, id=89)
        self.assertEqual(s.id, 89)

    def test_square_size(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_x(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_y(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(1, "2") # type: ignore

    def test_square_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3") # type: ignore

    def test_square_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_str(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")

    def test_square_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_square_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_create(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 8, "size": 10, "x": 7, "y": 2}]')

    def test_square_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s))


if __name__ == "__main__":
    unittest.main()
