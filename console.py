#!/usr/bin/python3
"""
This is the console that contains the entry point of the command interpreter.
"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class holds the console commands
    """
    prompt = "(hbnb)"

    def handle_input(self):
        if sys.stdin.isatty():
            return input(self.prompt)
        else:
            return input()

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        CTRL + D exits the command line interpreter
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER does nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new BaseModel instance
        """
        if not arg:
            print("** class name missing **")
            return
        new_instance = None
        try:
            class_name = arg
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            if new_instance:
                FileStorage.all().pop("{}.{}".format(class_name,
                                                     new_instance.id), None)
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        from models import storage
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and ID
        """
        from models import storage
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity",
                         "Place", "Review"]

        if class_name not in valid_classes:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                print("** class doesn't exist **")
                return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not
        on the class name
        """
        from models import storage
        if not arg:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)
        else:
            class_name = arg
            valid_classes = ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]

            if class_name not in valid_classes:
                print("** class doesn't exist **")
                return

            instances = [str(obj) for key, obj in storage.all().items()
                         if key.startswith(class_name)]
            print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute
        """
        from models import storage
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        valid_classes = ["BaseModel", "User", "State", "City",
                         "Amenity", "Place", "Review"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]

        current_value = getattr(storage.all()[key], attr_name, None)

        if current_value is not None:
            setattr(storage.all()[key], attr_name, type(current_value)
                    (attr_value))
        else:
            setattr(storage.all()[key], attr_name, type(attr_value)
                    (attr_value))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
