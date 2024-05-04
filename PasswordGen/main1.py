import random, string

def password(length,num=False,strength=True):
    """length of password, num if you want a number,
    and strength(weak,strong,very)"""

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        for i in range(length):
            pwd += random.choice(lower)
    return pwd

