from enigma import Enigma

rotor1 = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q"]
rotor2 = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"]  
rotor3 = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"]  
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  
plugs = ['AC', 'BE']  
settings = "AAA"
msg = "HELLOWORLD"
e = Enigma(rotor3, rotor2, rotor1, reflector)
ctxt = e.input(msg, ringsetting=settings, plugboard=plugs)
print(ctxt)
d = Enigma(rotor3, rotor2, rotor1, reflector)
ptxt = d.input(ctxt, ringsetting=settings, plugboard=plugs)
print(ptxt)
