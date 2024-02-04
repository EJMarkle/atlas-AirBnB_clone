#!/usr/bin/python3
"""
This is the console that contains the entry point of the command interpreter.
"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class holds the console commands
    """
    prompt = "(hbnb)"
    def do_quit(self, arg):
        """
        Exits the command interpreter
        """
        print("Goodbye!")
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
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.all():
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
