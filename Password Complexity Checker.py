import re

def a(p):
    pl = len(p)
    if pl < 8:
        return "Weak: Password should be at least 8 characters long."

    hu = bool(re.search(r'[A-Z]', p))
    hl = bool(re.search(r'[a-z]', p))
    hd = bool(re.search(r'\d', p))
    hs = bool(re.search(r'[^A-Za-z0-9]', p))

    me = []
    if not hu:
        me.append("uppercase letters")
    if not hl:
        me.append("lowercase letters")
    if not hd:
        me.append("numbers")
    if not hs:
        me.append("special characters")

    if me:
        return f"Password should include {', '.join(me)} to be stronger."
    else:
        return "Excellent: Password is very strong."

up = input("Enter your password: ")
psr = a(up)
print(psr)
