I. OVERVIEW

A state machine is a device or program that can store the status of something at a certain time. Based on input the status can change, providing the resulting output. 
State machines begin from what's called an initial state. A transition will take place based on provided inputs. Based on these inputs the user will move to other states which will also have transition functions; until an end state is reached



II. HOW DOES IT WORK?

First we need to define a dictionary called 'handlers' which will hold the various states, and references to their associated transition functions. Next we define a variable called 'startState' which will indicate the initial state of the machine. Finally we define a list object called 'endStates' which contains the names of the various end states. Shown below:

											   ###Containers###

		handlers = {}
		startState = None
		endStates = []


Next we need to call the 'addState' function which takes the following arguements: The name of the state, that state's transition function, and if the state is an end state.
Additionally the 'setStart' function sets the 'startState' variable to the name of the defined starting state (in this case "Start"). Shown below:

										  ###Creating State Instances###

		addState("Start", startTransition)
		addState("isState", isStateTransition)
		addState("positiveState", None, endState=True)
		setStart("Start")


Below are the 'addState' and 'setStart' functions, which are called, and given arguments from the lines above:

										   ###State Creation Methods###

		def addState(self, name, handler, endState=False):
			name = name.upper()
			self.handlers[name] = handler
			if endState:
				self.endStates.append(name)
				
		def setStart(self, name):
			self.startState = name.upper()
		
		
To run the state machine created above, the 'run' method must be called (shown below). The 'sentence' argument being passed contains the phrase "AI is" concatenated with the user's input (for this example we'll assume the user's input is "neat"). So the full sentence passed to the 'run' method is: "AI is neat".
	
										 ###Calling The 'run' Method###
										
		run(sentence)


The 'run' method (shown below) takes the sentence described above as an argument. From this point on, the sentence above will be refered to as 'userInput'.
In line 57 of the 'run' function below, the function associated with the 'startState' is called ('startTransition'), and the 'userInput' is passed as an argument. 

											 ###The 'run' Method###
												
		def run(self, userInput):
			handler = self.handlers[self.startState]
			while True:
				(newState, userInput) = handler(userInput)
				if newState.upper() in self.endStates:
					if newState == "errorState":
						print("Arrived at", newState, "(Unknown Adjective)")
					if newState != "errorState":
						print("Arrived at", newState)
					break 
				else:
					handler = self.handlers[newState.upper()]


At this point the user input is "AI is neat". Inside the transition function below the first word of 'userInput' is evaluated ("AI"), and based on the evaluated word the new state's name ('aiState') is assigned to the variable 'newState'. 
The remainder of the user input ("is neat"), along with the 'newState' variable ('aiState') are returned back to the 'run' method as 'newState' and 'txt'. 
		
											###Transition Function###
											
		def startTransition(txt):
			splitText = txt.split(None,1)
			word, txt = splitText if len(splitText) > 1 else (txt,"")
			
			if word == "AI":
				newState = 'aiState'
			else:
				newState = 'errorState'
			return (newState, txt)
			
			
Once 'newState' and 'txt' are returned to the 'run' method, the transition function associated with 'aiState' is called (line 59 of the 'run' method), and the user input "is neat" (returned from the transition function above) is passed to the next transition function ('aiStateTransition') where the process continues to repeat until all the words in the user's input are evaluated, or an end state is reached.



III. HOW IS THIS DATA STRUCTURE USEFUL?

State machines are used in many scientific applications; like modeling the behavior of applications, designing digital systems, software engineering, compilers, network protocols, and much more. The idea of going from one state to another based on some input is a foundation of modern computing.



IV. FURTHER READING

https://www.techopedia.com/definition/16447/state-machinehttps://www.bogotobogo.com/python/python_graph_data_structures.php
https://www.python-course.eu/finite_state_machine.php
https://www.geeksforgeeks.org/state-design-pattern/
https://en.wikipedia.org/wiki/Finite-state_machine
