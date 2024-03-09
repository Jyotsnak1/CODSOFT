import random
caps_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabets="abcdefghijklmnopqrstuvwxyz"
numerics="0123456789"
special_char="@#$%&*?"
combination=caps_alphabets+small_alphabets+numerics+special_char
passwd_length=9
password="".join(random.sample(combination,passwd_length))
print(password)