'''
CLASSY BOATS
-----------------
Use the following Pseudocode to create this program:

1.) Create a class called Boat( )
2.) Use a constructor that sets two attributes: name and isDocked.
3.) The name should be entered as an argument when the object is created.
4.) The isDocked attribute is a Boolean variable. Set it to True.
5.) Add a method called dock( )
6.) In this method, if the boat is already docked print "(boat name) is already docked."
7.) If it is not docked, print "(boat name) is docking" and set the isDocked attribute to True.
8.) Add another method called undock( )
9.) In this method, if the boat is already undocked print "(boat name) is already undocked."
10.) If it is docked print "(boat name) is undocking" and set the isDocked attribute to False.
11.) Add another class called Submarine( ) that will inherit the Boat( ) class.
12.) In the Submarine( ) class create a method called submerge( ) that will print "(boat name) is submerging" 
if the boat is undocked and "(boat name) can't submerge" if the boat is docked.

Let's Float the Boat
--------------------
13.) Instantiate an object of the Submarine( ) class. Don't forget to pass in a name.
14.) Call the dock( ) method once
15.) Call the undock( ) method twice
16.) Call the dock( ) method two more times
17.) Call the submerge( ) method once
18.) Call the undock( ) method once
19.) Call the submerge( ) method a final time.

OUTPUT:
USS Hermon is already docked.
USS Hermon is undocking
USS Hermon is already undocked.
USS Hermon is docking
USS Hermon is already docked.
USS Hermon can't submerge!
USS Hermon is undocking
USS Hermon is submerging!
'''


class Boat:
    def __init__(self, name, isDocked):
        self.name = name
        self.isDocked = True

    def dock(self):
        if self.isDocked:
            print("{} is already docked.".format(self.name))
        else:
            print("{} is docking.".format(self.name))
            self.isDocked = True

    def undock(self):
        if not self.isDocked:
            print("{} is already undocked.".format(self.name))
        else:
            print("{} is undocking.".format(self.name))
            self.isDocked = False

class Submarine(Boat):
    def __init__(self, name, isDocked):
        super().__init__(name, isDocked)
        self.name = name
        self.isDocked = True

    def submerge(self):
        if self.isDocked:
            print("{} can't submerge!".format(self.name))
        else:
            print("{} is submerging!".format(self.name))
            self.isDocked = True


subway = Submarine("Subway", True)
subway.dock()
subway.undock()
subway.undock()
subway.dock()
subway.dock()
subway.submerge()
subway.undock()
subway.submerge()

print("\n\n\nDid you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would "
      "tell you. "
      "It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the "
      "Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even"
      " keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some "
      "consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which "
      "eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice "
      "killed him in his sleep. Ironic. He could save others from death, but not himself.")
