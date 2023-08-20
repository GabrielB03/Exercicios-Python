from sqlite3 import TimestampFromTicks


temp = float(input("Digite a temperatura em graus Celsius: "))
tempF = 1.8 * temp + 32
tempK = temp + 273

print(f"A temperatura é equivalente a: {round(tempF,2)} °F")
print(f"e também é equivalente a: {round(tempK,2)} °K")