FROM osrf/ros:noetic-desktop

RUN apt-get update
RUN apt-get install -y git && apt-get install -y python3-pip

RUN mkdir -p ~/catkin_ws/src && \
    cd ~/catkin_ws/src/

COPY ./docker_pkg /root/catkin_ws/src/docker_pkg
RUN    cd ~/catkin_ws

RUN echo "ALL DONE!"
