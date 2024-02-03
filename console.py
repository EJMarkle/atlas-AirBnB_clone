#!/usr/bin/python3
"""
This is the console that contains the entry point of the command interpreter.
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
