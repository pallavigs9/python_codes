HappyArrSize, SetSize = map(int, raw_input('').split())

HappyArr = [int(n) for n in raw_input('').split()]

A = set()
B = set()
Ainput = [int(a) for a in raw_input('').split()]
Binput = [int(b) for b in raw_input('').split()]
if len(Ainput) and len(Binput) == SetSize:
    A.update(Ainput)
    B.update(Binput)

ACount = len(A.intersection(HappyArr))
BCount = len(B.intersection(HappyArr))
result = ACount - BCount
print result

'''
https://hr-testcases-us-east-1.s3.amazonaws.com/8382/input06.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1509479196&Signature=YiLrqT2kzZyPCvys%2BuHjWPwyqnk%3D&response-content-type=text%2Fplain

https://hr-testcases-us-east-1.s3.amazonaws.com/8382/output06.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1509479215&Signature=zkwMv7%2FtKBzw2t3bY2LNMFo0A1w%3D&response-content-type=text%2Fplain
'''