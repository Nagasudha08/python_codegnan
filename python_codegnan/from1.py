#single member 
from calculator import add 
from biology import genes 
from physics import newtonsfirst

# #module is not imported 
# print(calculator.add(20,10))
# print(biology.genes())
# print(physics.newtonsfirst())

#written memebers are imported
print(add(20,10))#30
print(genes())##Genes: Units of heredity that control traits
print(newtonsfirst())#First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force

# #other members are not imported
# print(sub(20,10))
# print(newtonssecond())
# print(dna())