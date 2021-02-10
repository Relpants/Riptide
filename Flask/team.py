class Team:
	def __init__(self):
		self.__name = ""	# __ double underscore indicates private member
		self.__logo = ""
		self.__score = 0
		self.__goalie = ("","")
	def setName(self, name):
		self.__name = name
	def setLogo(self, logo):
		self.__logo = logo
	def setScore(self, score):
		self.__score = score
	def setStartingGoalie(self, goalieName, savepct):
		self.__goalie = (goalieName, savepct)

	def getName(self):
		return self.__name
	def getLogo(self):
		return self.__logo
	def getScore(self):
		return self.__score
	def getStartingGoalie(self):
		return self.__goalie
