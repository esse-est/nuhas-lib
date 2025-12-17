
MEM={}

# bw
def BAND(foo:chr,bar:chr):
    """Bitwise AND"""
    return(chr(ord(foo) & ord(bar)))
def BXOR(foo:chr,bar:chr):
    """Bitwise XOR"""
    return(chr(ord(foo) ^ ord(bar)))
def BNOT(foo:chr):
    """Bitwise NOT"""
    return(chr(~ord(foo)))
def BORR(foo:chr,bar:chr):
    """Bitwise OR"""
    return(chr(ord(foo) | ord(bar)))
def BSSL(foo:chr):
    """Bitwise Static Shift Left"""
    return(chr(ord(foo)<<1))
def BSSR(foo:chr):
    """Bitwise Static Shift Right"""
    return(chr(ord(foo)>>1))
def BBIC(foo:chr,bar:chr):
    """Bitwise Bit Clear"""
    return (
        chr(ord(foo) & ~ord(bar))
    )

# arith
def AADD(foo:chr,bar:chr):
    """Arith Addition"""
    return(chr(ord(foo) + ord(bar)))
def AMIN(foo:chr,bar:chr):
    """Arith Subtraction"""
    return(chr(ord(foo) - ord(bar)))
def AMUL(foo:chr,bar:chr):
    """Arith Multiplication"""
    return(chr(ord(foo) * ord(bar)))

# manip

# comp/read

