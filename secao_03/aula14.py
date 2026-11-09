a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
string_position = 'a={0} b={1} c={2:.2f}'
string_parameter = 'a={a} b={b} c={c:.2f}'

formato = string.format(a, b, c)
formato_position = string_position.format(a, b, c)
formato_parameter = string_parameter.format(a=a, b=b, c=c)

print(formato)
print(formato_position)
print(formato_parameter)