#include <ros.h>
#include <std_msgs/Float32MultiArray.h>


#define pot_pin 5
#define trig_pin 2
#define echo_pin 4

unsigned long duration;
unsigned long distance;

int pot_input=0;

ros::NodeHandle nh;
std_msgs::Float32MultiArray array_data;


ros::Publisher sd_pub("/sensor_data", &array_data);




void setup() {
  // put your setup code here, to run once:
Serial.begin(57600);
pinMode(trig_pin, OUTPUT);
pinMode(echo_pin, INPUT);
pinMode(pot_pin, INPUT);

nh.initNode();
nh.advertise(sd_pub);
}

void loop() {
  // put your main code here, to run repeatedly:

pot_input=analogRead(pot_pin);
int pot_value=map(pot_input, 0, 255, 0.0, 1.0);

Serial.println(pot_value);

digitalWrite(trig_pin, LOW);
delayMicroseconds(2);
digitalWrite(trig_pin, HIGH);
delayMicroseconds(10);
digitalWrite(trig_pin, LOW);

duration=pulseIn(echo_pin, HIGH);
distance= duration*0.034/2;

Serial.print("distance: ");
Serial.print(distance);
Serial.println(" cm");


array_data.data[0]=pot_value;
array_data.data[1]=distance;

sd_pub.publish(&array_data);

nh.spinOnce();
delay(1000);

}
