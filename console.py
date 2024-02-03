#!/usr/bin/python3
"""
This is the console that contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_quit(self, arg):
        """
        Exits the command interpreter
        """
        print("Goodbye!")
        return True

    def do_EOF(self, arg):
        """
        Exits the command interpreter with CTRL-D
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
