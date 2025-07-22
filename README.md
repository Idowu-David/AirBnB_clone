# Description of the Project
This is an AirBnB Clone.

# Description of the Command Interpreter
The purpose of The Command Interpreter is to allow user to interact with this AirBnB Clone Program using commands in form of text lines. Such command in these case will be able to perfrom core actions like:
	
	- Create a new object (ex: a new User or a new Place)
	- Retrieve an object from a file, a database etc…
	- Do operations on objects (count, compute stats, etc…)
	- Update attributes of an object
	- Destroy an object

## How to start the shell
This is the  execution of the Shell in its ineractive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
And the Shell  execution in non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

![alt text](image.png)