def count_letter_a(input_string):
    # Lista de todas as variações de "a" que queremos considerar
    a_variants = ['a', 'á', 'à', 'â', 'ã', 'ä', 'A', 'Á', 'À', 'Â', 'Ã', 'Ä']
    
    # Contador de ocorrências
    count = sum(input_string.count(char) for char in a_variants)
    
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Solicita uma string ao usuário
user_input = input("Digite uma string: ")
count_letter_a(user_input)
