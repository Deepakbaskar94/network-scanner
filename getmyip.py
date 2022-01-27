# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# print(s.getsockname()[0])

import socket
print(socket.gethostbyname(socket.gethostname()))

# import socket
# def extract_ip():
#     st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:       
#         st.connect(('10.255.255.255', 1))
#         IP = st.getsockname()[0]
#     except Exception:
#         IP = '127.0.0.1'
#     finally:
#         st.close()
#     return IP
# print(extract_ip())