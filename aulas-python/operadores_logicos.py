saldo = 1000
saque = 250
limite = 200
conta_especial = True

# V and F or V and V
# V
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

# (V and F) or (V and V)
# F or V
# V
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
