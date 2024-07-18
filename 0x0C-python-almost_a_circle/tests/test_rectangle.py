import unittest
from unittest import mock
import io
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_id_auto(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_rectangle_id_passed(self):
        r = Rectangle(1, 2, id=89)
        self.assertEqual(r.id, 89)

    def test_rectangle_width_height(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_x(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_y(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3") # type: ignore

    def test_rectangle_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4") # type: ignore

    def test_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_rectangle_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display(self):
        r = Rectangle(2, 3)
        with mock.patch('sys.stdout', new_callable=io.StringIO)\
                as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), "##\n##\n##\n")

    def test_rectangle_display_with_x_y(self):
        r = Rectangle(2, 3, 2, 2)
        with mock.patch('sys.stdout', new_callable=io.StringIO)\
                as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_rectangle_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {
                                        'id': 1,
                                        'width': 10,
                                        'height': 2,
                                        'x': 1,
                                        'y': 9
                                    })

    def test_rectangle_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_create(self):
        r = Rectangle.create(**{
                            'id': 89,
                            'width': 1,
                            'height': 2,
                            'x': 3,
                            'y': 4
                        })
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_save_to_file(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                    file.read(),
                    '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_rectangle_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_file(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(r))


if __name__ == "__main__":
    unittest.main()
