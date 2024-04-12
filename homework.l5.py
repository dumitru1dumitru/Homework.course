# Aceasta este prima ta sarcină legată de liste

# Creează o listă goală numită `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = []
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în lista `numbers`
# CODUL TĂU VINE MAI JOS:
numbers.insert(0,1)
numbers.insert(1,2)
numbers.insert(2,3)
numbers.insert(3,4)
numbers.insert(4,5)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.append(6)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum șterge numărul 3 din lista `numbers`

# CODUL TĂU VINE MAI JOS:
del numbers[2]
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum sortează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.sort()
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum inversează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.reverse()         

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lungimea listei `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))
# CODUL TĂU VINE MAI SUS:

# Acum selectează primele două elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print(numbers[:2])
# CODUL TĂU VINE MAI SUS:

# Acum selectează ultimele trei elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print(numbers[-3:])
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 3 la poziția 2 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.insert(2,3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Creează o listă goală numită `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2 = []
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 6 la 10 în lista `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2 += [6, 7, 8, 9, 10, ]
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers2`

# CODUL TĂU VINE MAI JOS:
print(numbers2)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă lista `numbers2` la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = numbers + numbers2
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Acum transformă lista `numbers` într-un string și afișează-l

# CODUL TĂU VINE MAI JOS:
numbers_string = str(numbers)
print(numbers_string)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste






# Aceasta este a doua sarcină legată de tuples

# Creează un tuple numit `numbers` care să conțină numerele de la 1 la 5

# CODUL TĂU VINE MAI JOS:
numbers = (1, 2, 3, 4, 5)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la tuple `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = numbers + (6,)

# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Afișeați primul element din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[:1])
# CODUL TĂU VINE MAI SUS:   

# Afișeați ultimul element din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[-1:])
# CODUL TĂU VINE MAI SUS:

# Afișeați primele două elemente din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[:2])
# CODUL TĂU VINE MAI SUS:

# Afișeați ultimele două elemente din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[-2:])
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))
# CODUL TĂU VINE MAI SUS:

# Afișați suma elementelor din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(sum(numbers))
# CODUL TĂU VINE MAI SUS:

# Schibați elementul de la poziția 2 din tuple `numbers` cu 10

# CODUL TĂU VINE MAI JOS:
numbers_list = list(numbers)
numbers_list[2] = 10
numbers = tuple(numbers_list)
# CODUL TĂU VINE MAI SUS:

# Afișați tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Ștergeți tuple `numbers`

# CODUL TĂU VINE MAI JOS:
del numbers
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste