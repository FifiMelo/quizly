

result = 0
exec("""result = "".join(sorted(str(len(set(str(i)))) for i in range(10)))""")
print(result)