from pylibsshext.errors import LibsshSessionException
from pylibsshext.session import Session


ssh = Session()

HOST = 'CHANGEME'
USER = 'CHANGEME'
PASSWORD = 'CHANGEME'
TIMEOUT = 30
PORT = 22
try:
    ssh.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        timeout=TIMEOUT,
        port=PORT,
    )
except LibsshSessionException as ssh_exc:
    print(f'Failed to connect to {HOST}:{PORT} over SSH: {ssh_exc!s}')

print(f'{ssh.is_connected=}')

if ssh.is_connected:
    remote_file = '/etc/hosts'
    local_file = '/tmp/hosts'
    scp = ssh.scp()
    scp.get(remote_file, local_file)

    scp = ssh.scp()
    scp.put(local_file, remote_file)

ssh.close()
