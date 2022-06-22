import numpy as np
from Pyfhel import Pyfhel

HE = Pyfhel()
HE.contextGen(scheme='bfv',n=2**14,t_bits=20)
HE.keyGen()
print(HE)
integer1 = np.array([127],dtype=np.int64)
integer2 = np.array([-2],dtype=np.int64)
ctxt1 = HE.encryptInt(integer1)
ctxt2 = HE.encryptInt(integer2)
print("3. Integer Enctyption, ")
print("  int", integer1,'->ctx1',type(ctxt1))
print("  int", integer2,'->ctx2',type(ctxt2))
print(ctxt1)
print(ctxt2)

ctxtSum = ctxt1 + ctxt2
ctxtSub = ctxt1 - ctxt2
ctxtMul = ctxt1 * ctxt2
print("4. Operating with encrypted integers")
print(f"Sum: {ctxtSum}")
print(f"Sub: {ctxtSub}")
print(f"Mult: {ctxtMul}")

resSum = HE.decryptInt(ctxtSum)
resSub = HE.decryptInt(ctxtSub)
resMul = HE.decryptInt(ctxtMul)
print("addition: decrypt(ctxt1 + ctxt2) = ", resSum)
print("substraction: decrypt(ctxt1 - ctxt2) = ", resSub)
print("mutliplication: decrypt(ctxt1 * ctxt2) = ", resMul)
