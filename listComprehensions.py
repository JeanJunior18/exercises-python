# List Comprehension oferece vantagens de perfomance sobre o loop for
# É preciso bastante abstração para compreender 

lista = [1,2,3,4,5,6]

lst = [x for x in 'Python']
print(lst)

hard = [x for x in range(11) if x%2==0]
print(hard)