#include <Arduino.h>

/* BOARD INFO */
String DEVICE_NAME = "gate-1";

/* WIFI INFO */
String WIFI_SSID = "LiLy_2.4G";
String WIFI_PASSWORD = "@O53732i36";

/* MQTT INFO */
String MQTT_HOST = "mqtt.cmmc.io";
String MQTT_USERNAME = "";
String MQTT_PASSWORD = "";
String MQTT_CLIENT_ID = "";
String MQTT_PREFIX = "CMMC/NAT/";

int MQTT_PORT = 1883;
int PUBLISH_EVERY = 10L * 1000;
int MQTT_CONNECT_TIMEOUT = 10;
