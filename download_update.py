# Após dar run no code, existe um intervalo de tempo até sair o resultado, onde
# O código vai estar usando o site speedtest para verificar as informações.
from speedtest import Speedtest


st = Speedtest()

vel_download_bits = (st.download()/1024)/1024
vel_upload = (st.upload()/1024)/1024

print(f'O seu download: {vel_download_bits:.2f}MB/S')

print(f'O seu upload: {vel_upload:.2f}MB/S')
