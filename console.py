#!/usr/bin/python3
""" The entry point of the command interpreter """


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

classes = {
    "BaseModel": BaseModel,
    "User": User
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
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """
        Prints the string representaion of an instance
        based on the class name
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{args[1]}"
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return
        print(f"{all_objs[key]}")

    def do_destroy(self, arg):
        """ deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        idd = args[1]
        all_objs = storage.all()
        ids = [i.split(".")[1] for i in all_objs.keys()]
        if idd not in ids:
            print("** no instance found **")
            return
        clss = class_name + "." + idd
        del all_objs[clss]
        storage.save()

    def do_all(self, class_name=None):
        """
        Prints all string representation of all instances based or not
        on the class name
        """
        all_objs = storage.all()
        obj_list = []

        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            for key, value in all_objs.items():
                if key.split(".")[0] == class_name:
                    obj_list.append(str(value))
        else:
            for value in all_objs.values():
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the classname and `id` by adding
        or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        idd = args[1]
        all_objs = storage.all()
        ids = [i.split(".")[1] for i in all_objs.keys()]
        if idd not in ids:
            print("** no instance found **")
            return
        clss = class_name + "." + idd
        flag = False
        for model in all_objs.keys():
            # check whether the id matches the class name
            if model == clss:
                flag = True
                break
        if not flag:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except Exception:
            pass
        obj = all_objs[clss]
        setattr(obj, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
