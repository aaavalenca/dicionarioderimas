from mlconjug3 import Conjugator

# initialize the conjugator
conjugator = Conjugator(language="pt")

# conjugate the verb "parler"
verb = conjugator.conjugate("ser")

# print all the conjugated forms as a list of tuples.
print(verb.iterate())
