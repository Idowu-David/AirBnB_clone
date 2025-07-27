#!/usr/bin/python3
""" The entry point of the command interpreter """


import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program \n"""
        return True

    def do_EOF(self, arg):
        """ Exit (Ctrl+D) to exit the program """
        print("")
        return True
    
    def emptyline(self):
        """ Do nothing on empty input line """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
