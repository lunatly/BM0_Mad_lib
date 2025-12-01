
import random


story = random.randint(1,3)

verb = str(input('please enter a verb(action) word : '))
noun = str(input('please enter a noun(person,place,or thing) word : '))
adj = str(input('please enter a adjective(describes) word : '))

if story ==1:

	print(f'today i decided to {verb} to the park')
	print(f'when i arrrived i saw a very {adj} {noun} sitting on the bench')

if story ==2:

	print(f'I decided to {verb} at the popeyes')
	print(f'while there i was very {adj}')
	print(f'walking home i saw {noun}')

if story == 3:

	print(f'in twenty years im going to {verb} ')
	print(f'and in the future i discover a {adj} {noun}')