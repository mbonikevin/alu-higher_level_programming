#!/usr/bin/python3

"""Defines a foundational base model class."""
import json
import csv
import turtle


class Base:
    """Base class for managing id attributes and providing utility methods.

    This serves as the base for other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Keeps track of the number of Base instances created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Create a new Base instance.

        Args:
            id (int): An optional unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries into a JSON-formatted string.

        Args:
            list_dictionaries (list): A collection of dictionaries.
        Returns:
            str: JSON string representation of the list, or "[]" if the list is empty or None.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of object representations to a file in JSON format.

        Args:
            list_objs (list): Instances of the class to be serialized and written to the file.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string back into a Python list.

        Args:
            json_string (str): JSON string representing a list of dictionaries.
        Returns:
            list: Corresponding Python list, or an empty list if the input is None or empty.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Instantiate a class using attributes stored in a dictionary.

        Args:
            **dictionary (dict): Attribute-value pairs for initializing the instance.
        Returns:
            object: A new instance of the class with the specified attributes.
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)  # Placeholder dimensions for Rectangle
            else:
                obj = cls(1)  # Placeholder size for Square
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Load and return a list of class instances from a JSON file.

        Reads from a file named `<cls.__name__>.json`.

        Returns:
            list: A list of instantiated objects, or an empty list if the file does not exist.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of object representations to a file in CSV format.

        Args:
            list_objs (list): Instances of the class to be serialized and written to the file.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:  # Square
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load and return a list of class instances from a CSV file.

        Reads from a file named `<cls.__name__>.csv`.

        Returns:
            list: A list of instantiated objects, or an empty list if the file does not exist.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:  # Square
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                    {k: int(v) for k, v in d.items()} for d in reader
                ]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Use the turtle module to draw rectangles and squares.

        Args:
            list_rectangles (list): A collection of Rectangle objects to draw.
            list_squares (list): A collection of Square objects to draw.
        """
        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")  # Set the background color
        t.pensize(3)  # Set the pen thickness
        t.shape("turtle")  # Use a turtle shape cursor

        # Draw rectangles
        t.color("#ffffff")
        for rectangle in list_rectangles:
            t.showturtle()
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.hideturtle()

        # Draw squares
        t.color("#b5e3d8")
        for square in list_squares:
            t.showturtle()
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()  # Close the turtle window on click
