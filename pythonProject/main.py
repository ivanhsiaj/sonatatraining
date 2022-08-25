from leave import Leave
from basketofleave import BasketOfLeave
from restrictedleave import RestrictedLeave
r1=RestrictedLeave(22790,"Jaishu",20,"2000-06-20")
print(r1.display_dob())
b1=BasketOfLeave(22790,"Jaishu",20,1)
print(b1.display())
print(b1.displayleave())