class English:
	def greet(self,name):
		print('Good Morning', name)

class French:
	def greet(self, name):
		print('Bonjour', name)

class German:
	def greet(self, name):
		print('Guten Morgan', name)

def greetings(language, name):
	language.greet(name)

print('1.English\
	   2.French\
	   3.German\
	   4.Enter 4 to quit')

name = input('Enter ur name...')

language = input('Enter in which language to greet you...')

if language.lower()=='english':
	english = English()
	greetings(english, name)

if language.lower()=='french':
	french = French()
	greetings(french, name)
	
if language.lower()=='german':
	german = German()
	greetings(german, name)