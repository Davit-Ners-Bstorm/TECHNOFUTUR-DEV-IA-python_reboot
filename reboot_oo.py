from models.elephant import Elephant
from models.soigneur import Soigneur

soigneur1 = Soigneur("Fabian", 1989)

el1 = Elephant('Dumbo', soigneur1)

print([el1])
print(el1.__dict__)
