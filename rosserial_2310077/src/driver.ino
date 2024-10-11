#include <ros.h>
#include <geometry_msgs/Twist.h>

const int ENA=4;
const int ENB=7;
const int IN1=2;
const int IN2=3;
const int IN3=5;
const int IN4=6;

ros::NodeHandle nh;

 

void motor_callback(const geometry_msgs::Twist& velocity){
  float forward= velocity.linear.x;
  float left=velocity.angular.z;

  int motor_forward=map(forward, 0.0, 1.0, 0, 255);
  int motor_backward=map(left, 0.0, 1.0, 0, 255);

  if (velocity.linear.x!=0){ 
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(4, motor_forward);
    analogWrite(7, motor_forward);  
    }

  else{
   digitalWrite(IN1, LOW);
   digitalWrite(IN2, HIGH);
   digitalWrite(IN3, HIGH);
   digitalWrite(IN4, LOW);
   analogWrite(4, motor_backward);
   analogWrite(7, motor_backward);
   }

}
  
  
  
  ros::Subscriber<geometry_msgs::Twist> motor_sub("/cmd_vel", &motor_callback);
  


void setup() {
  // put your setup code here, to run once:
 pinMode(2, OUTPUT);
 pinMode(3, OUTPUT);
 pinMode(4, OUTPUT);
 pinMode(5, OUTPUT);
 pinMode(6, OUTPUT);
 pinMode(7, OUTPUT);

 nh.initNode();
 nh.subscribe(motor_sub);
 
}

void loop() {
  // put your main code here, to run repeatedly:
nh.spinOnce();
delay(1);
}
