#  Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.


# luciano resolveu usando uma função set()
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

##############
only = list()
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
for email in emails:
    if email not in only:
        only.append(email)
print(f'Os emails únicos são: {only}')