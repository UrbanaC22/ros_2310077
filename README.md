# Guide to using Husarnet
  Husarnet is a Peer-to-Peer VPN using which several devices, microcontrollers, servers can be connected over the Internet. For ERC Remote 2025, Husarnet is going to be the means of communication between the robots provided by
  the operator(Husarion) and the devices of the participants. 

#### A video demonstrating the operation of Husarnet can be found at https://drive.google.com/file/d/1tWuOgJ2B7OfTShkfv-i7IGnrBolxqNka/view?usp=drive_link

## Husarnet Network

### Creating a Husarnet account
   Create a Husarnet account by going to https://app.husarnet.com. Go to the dashboard and click on "Create Network" to create a new network. Click on the network and under "Add element", a Join Code will appear which is the 
   means of connecting to the network.

### Joining a Network
   Using the Join Code, any remote device will be able to join the network. First of all, Husarnet needs to be installed on the device by executing the following command:
   ```
   curl -s https://install.husarnet.com/install.sh | sudo bash
   ```
   Then the network can be joined using:
   ```
   sudo husarnet join <Join Code> <hostname>
   ```
   After the device successfully connects to the network, the other devices in the network can be pinged by executing
   ```
   ping6 <hostname>
   ```
   in the terminal.
   Likewise, groups containing multiple networks can be joined using the Join Code.

## Controlling a robot using Husarion WebUI
   Install Husarion WebUI on your device by executing the following command in the terminal:
   ```
   sudo snap install husarion-webui
   ```
   #### Note:
   If snap is not previously installed on the device, install it using:
   ```
   sudo apt update
   sudo apt install snapd
   ```
   Alternatively, you can also install the WebUI from https://snapcraft.io/husarion-webui and set the parameters and configure the WEBUI according to the instructions provided in the website.

   Start the WebUI using the following command:
   ```
   sudo husarion-webui.start
   ```
   The WebUI can then be accessed by entering this address in your web browser: http://localhost:8080/ui .
   Upon launching the Gazebo simulation, the robot can be controlled using the WebUI.

   To stop the WebUI, use
   ```
    sudo husarion-webui.stop
   ```

## Conneting ROS2 via Husarnet
   Husarnet can be used for the communication of ROS2 nodes running in several devices connected to the same network. Although a discovery server is to be used for the ERC Remote 2025, until further clarification from
   the operator, the custom CycloneDDS xml env shall be used for the demonstration. Other methods to connect the ROS2 nodes can be found at https://husarnet.com/docs/tutorial-ros2/

   To create the custom CycloneDDS file execute the following commands:
   ```
   cd //var/tmp
   touch cyclonedds.xml
   open cyclonedds.xml
   ```

   Paste the following:
   ```
   <?xml version="1.0" encoding="UTF-8" ?>
   <CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
     <Domain Id="any">
        <General>
            <Interfaces>
                <NetworkInterface name="hnet0"/>
            </Interfaces>
            <AllowMulticast>false</AllowMulticast>
            <FragmentSize>1194B</FragmentSize><!-- default: 1344 B minus Husarnet metadata (~150 B) -->
            <Transport>udp6</Transport>
        </General>      
        <Discovery>
            <Peers>
                <Peer Address="talker-host" /> <!-- or <Peer address="fc94:a67f:2b47:756c:6e1c:7c05:7361:7378"/> -->
                <Peer Address="listener-host" /> <!-- or <Peer address="fc94:6260:26e:e057:9bc:8786:4f8a:c7a6"/> -->
            </Peers>
            <ParticipantIndex>auto</ParticipantIndex>
            <MaxAutoParticipantIndex>40</MaxAutoParticipantIndex>
        </Discovery>
     </Domain>
  </CycloneDDS>
 ```
 Replace "talker-host" and "listener-host" with the hostnames in the network and manually add the other hostnames using new <Peer> tags.
 Install the RMW implementation:
 ```
 sudo apt install ros-humble-rmw-cyclonedds-cpp
 ```
 Then export the implementation and file by executing the following command in the terminal:
 ```
 export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
 export CYCLONEDDS_URI=file:///var/tmp/cyclonedds.xml
 ```
 #### Note:
 Export the above everytime a new terminal is opened.

 Repeat the procedure on all the host devices to be connected.
 To check the connectivity, a string can optionally be published to a topic by executing:
 ```
 ros2 topic pub /hello std_msgs/String "data: Hello"
 ```
 Echo the topic from any other device in the Husarnet network connected using CycloneDDS to ensure connectivity:
 ```
 ros2 topic echo /hello
 ```
 After the ROS2 nodes have been connected, the Gazebo simulation can be run in one of the devices and remotely controlled using a GUI from another, for example.

 More information about Husarnet can be found at https://husarnet.com/docs/
 
 
   
   
  

     
