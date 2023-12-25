import subprocess
import unittest
def connect_server(ip_address):
    try:
        command = ['iperf', '-c', ip_address]
        #print(command)

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        return result.stdout, result.stderr

    except subprocess.CalledProcessError as e:
        return None, f"Error: {e.stderr}"

class Test(unittest.TestCase):
    def test_iperf_connection(self):
        ip_address = "10.0.2.5"

        output, error = connect_server(ip_address)
        # print("iperf Error:", error)
        print("Output:", output)
        print("Error:", error)

if __name__ == "__main__":
    unittest.main()