import argparse
import re
def format_line(line,max_length):
  if len(line)<=max_length:
    return[line]
  else:
    break_point=line.rfind(" ",0,max_length)
    if break_point==-1:
      break_point=max_length
    return[line[:break_point]]+format_line(      line[break_point:].lstrip(),max_length    )
def format_quotes(input_file,max_line_length=79):
  try:
    with open(input_file,"r")as f:
      code=f.read()
    pattern=r'(""".*?""")'
    matches=re.finditer(pattern,code,re.DOTALL)
    for match in reversed(list(matches)):
      old_text=match.group(0)
      text_content=old_text[        3:-3      ].strip()
      lines=text_content.split("\n")
      new_lines=[]
      for line in lines:
        new_lines.extend(format_line(line,max_line_length))
      new_text='"""\n'+"\n".join(new_lines)+'\n"""'
      code=code[:match.start()]+new_text+code[match.end():]
    with open(input_file,"w")as f:
      f.write(code)
  except IOError as e:
    print(f"Erro ao abrir o arquivo: {e}")
def main():
  parser=argparse.ArgumentParser(    description="Formata as aspas triplas em um arquivo Python."  )
  parser.add_argument("input_file",help="Nome do arquivo Python a ser formatado.")
  args=parser.parse_args()
  format_quotes(args.input_file)
if __name__=="__main__":
  main()