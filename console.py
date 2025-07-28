#!/usr/bin/python3
""" The entry point of the command interpreter """


import cmd
from models.base_model import BaseModel
from models import storage

classes = {
    "BaseModel": BaseModel
}

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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if not arg:
            print(f"** class name missing **")
        elif arg not in classes:
            print(f"** class doesn't exist **")
        else:
            new = classes[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """ Prints the string representaion of an instance based on the class name """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print(" ** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        idd = args[1]
        dicts = storage.all()
        ids = [i.split(".")[1] for i in dicts.keys()]
        if idd not in ids:
            print("** no instance found **")
            return
        clss = class_name + "." + idd
        print(f"{dicts[clss]}")

    def do_destroy(self, arg):
        """ deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print(" ** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        idd = args[1]
        dicts = storage.all()
        ids = [i.split(".")[1] for i in dicts.keys()]
        if idd not in ids:
            print("** no instance found **")
            return
        clss = class_name + "." + idd
        del dicts[clss]
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
