from pythonosc import udp_client
import time

# OSCサーバーのアドレスとポートに合わせて設定
osc_server_ip = '0.0.0.0'
osc_server_port = 8000

# OSCクライアントを作成
client = udp_client.SimpleUDPClient(osc_server_ip, osc_server_port)

# OSCメッセージを送信する例
address = '/VMC/Ext/Root/Pos'
args = ['root', -0.037, -0.090, 0.596, 0.000, 0.000, 0.000, 1.000]
client.send_message(address, args)

time.sleep(1)

address = '/VMC/Ext/Bone/Pos'
args = ['leftUpperLeg', -0.037, -0.090, 0.596, 0.000, 0.000, 0.000, 1.000]
client.send_message(address, args)

time.sleep(1)

address = '/VMC/Ext/Bone/Pos'
args = ['leftLowerLeg', -0.037, -0.090, 0.596, 0.000, 0.000, 0.000, 1.000]
client.send_message(address, args)

time.sleep(1)

address = '/VMC/Ext/Root/Pos'
args = ['root', -0.037, -0.090, 0.596, 0.000, 0.000, 0.000, 1.000]
client.send_message(address, args)