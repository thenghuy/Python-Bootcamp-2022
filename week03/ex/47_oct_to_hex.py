def oct_to_hexa(number):
      for ch in str(number):
            if (ch < '0' or ch > '7'):
                  print("This is not an octal number")
                  return
      dec_num = int(str(number), 8)
      hexa_num = hex(dec_num).replace("0x", "")
      print(hexa_num.upper())
oct_to_hexa(1271)