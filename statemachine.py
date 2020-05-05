#The functions below display aditional process information if the user requests.
firstUse = 0
info = False
def endStateInfo(word, newState):
	if info == True: print("The function above evaluated the word '"+ word + "'.  Arrived at: '" + newState +"'. Which is an end state\n")
	else: pass
def regStateInfo(word, newState, txt):
	if info == True: print("The function above evaluated the word '"+ word + "'.  Arrived at: '" + newState +"'.  Passing: '" + txt + "' to the function below:")
	else: pass
	
	

class StateMachine:
	def __init__(self):
		self.handlers = {} #Contains the names of the various states, and the transition functions associated with them.
		self.startState = None #Contains the start state.
		self.endStates = [] #Contains the possible end states.
		
#Function for adding a state & it's transition function to the 'handlers' dictionary. Takes the name, transition function, and whether or not the declared state is an end state as arguments.
	def addState(self, name, handler, endState=False):
		name = name.upper()
		self.handlers[name] = handler
		if endState:
			self.endStates.append(name)

#Function for defining the start state.
	def setStart(self, name):
		self.startState = name.upper()

#Function that initiates the state traversal algorithm (line 32). Also takes arguments from transition functions, and calls the next function based on those arguments (line 34). Once a state defined as an end state is reached it prints the final state, and breaks the loop.
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
				if info == True: print(handler)



#Adjective lists
positiveAdjectives = ["clean", "good", "great", "entertaining", "sweet", "nice", "dope", "terrific", "fun", "cool", "neat", "intriguing", "positive"]
negativeAdjectives = ["poop", "hard", "ugly", "bad", "difficult", "awful", "terrible", "gross", "foolish", "dumb", "negative", "stupid", "scary", "troubling", "dangerous"]

#Holds names of the states that have been visited to display to the user once the run completes.
statesTraversed = ""


#The function below parses the sentence "...AI is (userInput)", if the word "AI" is present, it will return the 'aiState' and pass the rest of the sentence to the 'aiStateTransition' function. If "AI" is not present, it will return the 'errorState'.
def startTransition(txt):
	global statesTraversed
	splitText = txt.split(None,1)
	word, txt = splitText if len(splitText) > 1 else (txt,"")
	
	if word == "AI":
		newState = "aiState"
		statesTraversed = statesTraversed + (newState) + " -> "
		if info == True:
			print("The 'startTransition' function evaluated the word '"+ word + "'.  Arrived at: '" + newState +"'. Passing: '" + txt + "' to the function below:")	
	else:
		newState = "errorState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
		endStateInfo(word, newState)
	return (newState, txt)


#The function below parses the rest of the sentence, if the word "is" is present, it will return the 'isState', and pass the rest of the sentence to the 'isStateTransition' function. If "is" is not present, it will return the 'errorState'.
def aiStateTransition(txt):
	global statesTraversed
	splitText = txt.split(None,1)
	word, txt = splitText if len(splitText) > 1 else (txt,"")
	
	if word == "is":
		newState = "isState"
		statesTraversed = statesTraversed + (newState) + " -> "
		regStateInfo(word, newState, txt)
	else:
		newState = "errorState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
		endStateInfo(word, newState)
	return (newState, txt)


#The function below parses the rest of the sentence; if the word "not" is present, it will return the notState, and pass the rest of the sentence (which should be the last word) to the 'notStateTransition'. If the word "not" is not present it will return either the 'positiveState' or the 'negativeState' depending on whether the next word is in the 'positiveAdjectives' or 'negativeAdjectives' lists. If the next word isnt in either list, it will return the 'errorState'.
def isStateTransition(txt):
	global statesTraversed
	splitText = txt.split(None,1)
	word, txt = splitText if len(splitText) > 1 else (txt,"")
	
	if word == "not":
		newState = "notState"
		statesTraversed = statesTraversed + (newState) + " -> "
		regStateInfo(word, newState, txt)
	elif word in positiveAdjectives:
		newState = "positiveState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
		endStateInfo(word, newState)
	elif word in negativeAdjectives:
		newState = "negativeState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
		endStateInfo(word, newState)
	else:
		newState = "errorState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
		endStateInfo(word, newState)
	return (newState, txt)


#Since this function is performed after the word "not" is detected it will return the 'negativeState' if the next word is present in the 'positiveAdjectives' list; or the 'positiveState' if the next word is present in the 'negativeAdjectives' list. If the user's input is not present, it will return the 'errorState'.
def notStateTransition(txt):
	global statesTraversed
	splitText = txt.split(None,1)
	word, txt = splitText if len(splitText) > 1 else (txt,"")
	
	if word in positiveAdjectives:
		newState = "negativeState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
	elif word in negativeAdjectives:
		newState = "positiveState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
	else:
		newState = "errorState"
		statesTraversed = statesTraversed + (newState) + " (End State)"
	endStateInfo(word, newState)
	return (newState, txt)



if __name__== "__main__":
	m = StateMachine()
	m.addState("Start", startTransition)				#Declare state, and transition function
	m.addState("aiState", aiStateTransition)			#Declare state, and transition function
	m.addState("isState", isStateTransition)			#Declare state, and transition function
	m.addState("notState", notStateTransition)			#Declare state, and transition function
	m.addState("negativeState", None, endState=True)	#Declare end state
	m.addState("positiveState", None, endState=True)	#Declare end state
	m.addState("errorState", None, endState=True)		#Declare end state
	m.setStart("Start")									#Declare the start state
	
	print("Enter a positive or negative adjective that completes the following sentence:")
	print("\nFor Example:")
	print("Positive: 'great' 'neat' 'not bad' 'not scary' \nNegative: 'bad' 'scary' 'not great' 'not neat'\n")

#User choice for process information	
	while True:
		if firstUse == 1:
			moreInfo = input("Would you like to see more detail on the processes at work? Y/N: ")
			if moreInfo == 'Y'or moreInfo == 'y':
				info = True
			else:
				pass
				
#User prompt without examples
		if firstUse != 0:
			statesTraversed = ""
			print("\n \nEnter a positive or negative adjective that completes the following sentence:")
		firstUse = firstUse + 1
		usrInput = input("I think AI is ")
		print("")
		if info == True: print("Information:")
		sentence = "AI is " + str(usrInput.lower())

#Calls the function that initiates the state traversal sequence, with the sentence containing the user's input.
		m.run(str(sentence))	

#Prints the names of the states that were visited during the traversal process.
		print("States traversed: "+ str(statesTraversed))
				
#Try again prompt
		res = input("\nTry again? Y/N: ")
		if res == 'N'or res == 'n':
			print("\nBye!")
			break
