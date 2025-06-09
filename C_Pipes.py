# T = int(input())


# def solve(s):

#     pos = 0 
#     row = 0 
#     while pos < len(s[0]):
#         if s[row][pos] >="3":
#             if s[row^1][pos] < "3":
#                 break
#             else:
#                 row= row^1
#         pos+=1
    
#     if pos==len(s[0]) and row==1:
#         print("YES")
#     else:
#         print("NO")

#     pass



# for _ in range(T):
#     n = int(input())
#     s = [] 
#     s.append(input())
#     s.append(input())
#     solve(s)

# def cal(x):
#     if x<0:
#         return x**4
#     else:
#         return 0 

# def solve(n):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     if len(arr)!=n:
#         print(-1)
#     else:
#         print(sum(list(map(cal,arr))))


# def main():
    
#     N = int(input())
#     list(map(solve,range(N)))
    
#     pass


# if __name__ =="__main__":
#     main()

# import base64
# import hashlib
# import hmac
# import struct
# import time

# def generate_totp(secret, time_step=30, digits=10, algo=hashlib.sha512):
#     current_time = int(time.time())
#     counter = current_time // time_step
#     key = secret.encode()
#     msg = struct.pack(">Q", counter)
#     hmac_digest = hmac.new(key, msg, algo).digest()
#     offset = hmac_digest[-1] & 0x0F
#     code = (struct.unpack(">I", hmac_digest[offset:offset+4])[0] & 0x7fffffff) % (10 ** digits)
#     return str(code).zfill(digits)

# # Replace with your actual email
# email = "aditya789arora@gmail.com"
# secret = email + "HENNGECHALLENGE004"
# print("TOTP Code:", generate_totp(secret))
