class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class E(B,C):
    pass

class F(D):
    pass

class G(E):
    pass

class H(F,G):
    pass

print(H.mro())