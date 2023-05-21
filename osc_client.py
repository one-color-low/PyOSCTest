from pythonosc import udp_client

# OSCサーバーのアドレスとポートに合わせて設定
osc_server_ip = '0.0.0.0'
osc_server_port = 8000

# OSCクライアントを作成
client = udp_client.SimpleUDPClient(osc_server_ip, osc_server_port)

# OSCメッセージを送信する例
address = '/example/address'
args = [1, 2, 3.14, 'hello']
client.send_message(address, args)
