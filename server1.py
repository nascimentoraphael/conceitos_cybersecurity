msg = input("Please enter your message ")

key = "abcdefghijklmnopqrstuvwxyz0123456789 !"
val = key[:: -1]

e_msg = dict(zip(key , val))
# print(e_msg)

enc_msg = "".join([e_msg[words] for words in msg.lower()])

print((enc_msg))

derripter = dict(zip(val , key))

dec_msg = "".join([e_msg[words] for words in enc_msg.lower()])

print((dec_msg))