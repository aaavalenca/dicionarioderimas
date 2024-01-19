from mlconjug3 import Conjugator
import mlconjug3

# initialize the conjugator
conjugator = Conjugator(language="pt")

verb = conjugator.conjugate("ser")

print(verb['Indicativo'])
