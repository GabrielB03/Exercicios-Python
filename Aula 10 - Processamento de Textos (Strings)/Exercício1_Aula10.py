print("Entrada: ")

email = input("Digite o seu e-mail: ")
acharDominio = email.find("@") + 1
dominio = "http://" + email[acharDominio: :]

print("\nSaída: ")
print(f"\nO domínio do seu e mail é {dominio}")