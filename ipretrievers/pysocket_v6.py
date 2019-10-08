import socket

# Inspired by https://codeday.me/en/qa/20190306/6413.html
def get_ip_6(host, port=0):
    import socket
    # search only for the wanted v6 addresses
    result = socket.getaddrinfo(host, port, socket.AF_INET6)
    #return result # or:
    return result[0][4][0] # just returns the first answer and only the address


def getIP():
	try:
		return get_ip_6(socket.gethostname())
	except CalledProcessError as err:
		print("ERROR: Failed to retrieve IPv6 address: " + str(err))
		return None
