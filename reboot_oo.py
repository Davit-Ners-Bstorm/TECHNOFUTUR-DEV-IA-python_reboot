from models.elephant import Elephant
from models.soigneur import Soigneur
from models.girafe import Girafe

soigneur1 = Soigneur("Fabian", 1989)

el1 = Elephant('Dumbo', soigneur1, 30)
# girafe1 = Girafe()


print([el1])
print(el1.__dict__)
