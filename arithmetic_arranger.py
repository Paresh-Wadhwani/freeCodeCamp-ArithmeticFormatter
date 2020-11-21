def arithmetic_arranger(problems, boolarg = False):
  if len(problems) > 5:
    return "Error: Too many problems."
  if str(problems).find('*') > 0 or str(problems).find('/') > 0:
    return "Error: Operator must be '+' or '-'."

  operand1s = []
  operators = []
  operand2s = []
  maxlens = []
  ans = []
  dasharr = []
  op1 = ""
  op2 = ''
  ansstr = ''
  dashstr = ''
  
  for i in problems:
    x = i.find(' ')
    y = i.find(' ', x + 1)
    operand1 = i[:x]
    operator = i[x + 1:y]
    operand2 = i[y + 1:]
    if operand1.isnumeric() == False or operand2.isnumeric() == False:
      return "Error: Numbers must only contain digits."
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."
    maxlen = max(len(operand1), len(operand2))
    maxlens.append(maxlen)

    o1 = ' '*(maxlen - len(operand1)) + operand1
    o2 = ' '*(maxlen - len(operand2)) + operand2

    operand1s.append(o1)
    operators.append(operator)
    operand2s.append(o2)
    an = str(int(operand1) + int(operand2)) if operator == '+' else str(int(operand1) - int(operand2))
    an = ' '*(maxlen + 2 - len(an)) + an
    ans.append(an)
    dasharr.append('-'*(maxlen+2))

  for j in range(0, len(problems)):
    if op1 == '':
      op1 = '  ' + operand1s[j]
    else:
      op1 = op1 + '      ' + operand1s[j]

    if op2 == '':
      op2 = operators[j] + ' ' + operand2s[j]
    else:
      op2 = op2 + '    ' + operators[j] + ' ' + operand2s[j]

    if ansstr == '':
      ansstr = ans[j]
    else:
      ansstr = ansstr + '    ' + ans[j]
    
    if dashstr == '':
      dashstr = dasharr[j]
    else:
      dashstr = dashstr + '    ' + dasharr[j]

  arranged_problems = (op1 + '\n' + op2 + '\n' + dashstr + '\n' + ansstr) if boolarg else (op1 + '\n' + op2 + '\n' + dashstr)

  return arranged_problems