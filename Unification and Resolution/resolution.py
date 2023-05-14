from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, Implies
from sympy.logic.inference import satisfiable

# Step 1: Define the symbols
john_likes = symbols('john_likes')
peanuts = symbols('peanuts')
anil_eats = symbols('anil_eats')
harry_eats = symbols('harry_eats')

# Step 2: Define the knowledge base
knowledge_base = And(
    Implies(john_likes, peanuts),  # John likes peanuts
    Implies(anil_eats, peanuts),  # Anil eats peanuts
    Implies(harry_eats, anil_eats),  # Harry eats everything that Anil eats
    Implies(john_likes, harry_eats)  # John likes what Harry eats
)

# Step 3: Define the negation of the statement to be proved
negation = Not(john_likes)

# Step 4: Combine the knowledge base and negation
clauses = And(knowledge_base, negation)

# Step 5: Check if the clauses are satisfiable (i.e., if the negation is false)
model = satisfiable(clauses)

# Step 6: Check if the negation is unsatisfiable (i.e., if it is not possible for it to be false)
if not model:
    print("John likes peanuts can be proven by resolution.")
else:
    print("John likes peanuts cannot be proven by resolution.")
