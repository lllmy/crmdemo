from django.test import TestCase

# Create your tests here.
# c = lambda x:x**2
# print(c(2))
# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%s*%s=%s"%(y,x,x*y),end=" ")
#     print()
print('\n'.join(['\t'.join(["%s*%s=%s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))
print("\n".join(['\t'.join(["%s*%s=%s" % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
