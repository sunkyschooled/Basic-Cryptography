from base64 import b64encode, b64decode

def single_byte_xor(message, key, mode='encrypt'):
  encrypt = mode == 'encrypt'
  if encrypt:
    ba = bytearray(message, encoding='ASCII')
  else:
    ba = bytearray(b64decode(message))
  
  new_ba = bytearray()
  for b in ba:
    new_ba.append(b ^ key)
  
  if encrypt:
    return b64encode(new_ba)
  else:
    return new_ba.decode("ASCII")