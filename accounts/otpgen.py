import random as r
from datetime import time, datetime, timedelta


def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    # print (otp)
    return(otp)

def otptime():
    current_time = datetime.now();
    expire_time = current_time + timedelta(minutes=2)
    print(expire_time - current_time)
    print(otpgen())