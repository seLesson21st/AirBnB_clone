#!/usr/bin/python3
""" The console module """
import cmd
import sys

class Hbnbcommand(cmd.Cmd):
    intro = "Welcome to my HBNB, it contains all the systems of my Console type 'help' for more commands\n"
    prompt = "myhbnh>>>"
    """if sys.__stdin__.isatty() else ''"""

    def preloop(self):
        """ Prints isatty is false """
    if not sys.__stdin__.isatty():
        print("myhbnb")

    def do_EOF(self, args):
        """Helps EOF to exit"""
        return True

    def help_EOF(self):
        """Prints the EOF hep documentatio"""
        print("Exiting program without formatting\n")

    def emptyline(self):
        """Overrides the Cmd emptyline"""
        pass

    def do_quit(self, args):
        """ Exits myhbnb console """
        return True

if __name__ == "__main__":
    Hbnbcommand().cmdloop()
