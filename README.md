# CMSC137_AB1L_Project
CMSC 137 Project by Castillo, Fernandez, Maliksi, and Sartillo

How to run:<br>
  For server:<br>
    <ol>
      <li>Check the IP address of the system (use ifconfig or the likes).</li>
      <li>Run 'python3 server.py' on Linux or 'python server.py' on Windows.</li>
      <li>Enter '1' and input the IP address of the server.</li>
      <li>Input port number. The program will try to bind to the IP address and port number and will ask for another port number if it returns an error.</li>
      <li>Enter number of players that will enter.</li>
      <li>Wait for the clients to connect.</li>
    </ol>
  For client:<br>
    <ol>
      <li>Run 'python3 client.py' on Linux or 'python client.py' on Windows.</li>
      <li>Enter '1' and input the IP address of the server. This must be exactly the same with what you entered for the server</li>
      <li>Input port number. This must also be the same with what you entered for the server.</li>
      <li>Enter your name.</li>
      <li>Wait for other clients to enter if the number of players has not been met yet.</li>
    </ol>
