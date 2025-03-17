FROM osrf/ros:noetic-desktop-full

RUN apt-get update 

RUN apt-get install -y git && apt-get install -y python3-pip

RUN mkdir -p ~/catkin_ws/src && \
    cd ~/catkin_ws/src/
    
COPY ./src /catkin_ws/src 

RUN cd ~/catkin_ws

RUN echo "ALL DONE"
