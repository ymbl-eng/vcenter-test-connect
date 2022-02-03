import atexit
import ssl

from pyVim import connect
from pyVmomi import vmodl

# vCenter接続情報
host="vcsa.vsphere.local" #vCenterのIP又はホスト名
user="administrator@vsphere.local" #vCenterのログインユーザー名
password="password" #vCenterのログインユーザーパスワード
port=443

def main():

	try:
		_create_unverified_https_context = ssl._create_unverified_context
	except AttributeError:
		pass
	else:
		ssl._create_default_https_context = _create_unverified_https_context

	try:
		service_instance = connect.SmartConnect(host=host,
                                                user=user,
                                                pwd=password,
                                                port=port)

		atexit.register(connect.Disconnect, service_instance)
		print("vCenterへの接続が確認できました")
		
	except vmodl.MethodFault as error:
		print("Caught vmodl fault : " + error.msg)
		return -1
	return 0
	
if __name__ == "__main__":
    main()
