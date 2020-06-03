from SCons.Script import DefaultEnvironment
import glob, shutil, os
import time

env = DefaultEnvironment()
# env.Replace(PROGNAME="firmware_%s" % defines.get("VERSION"))
# uncomment line below to see environment variables
# print env.Dump()
# print ARGUMENTS

# copyfile("src/MqttConnector.h", "tmp/MqttConnector/MqttConnector.h")
# copyfile("src/MqttConnector.cpp", "tmp/MqttConnector/MqttConnector.cpp")

print "BEING COPY FILES..."
# shutil.rmtree("pio_compile_here/MqttConnector",  ignore_errors=True) 
# time.sleep(2)
if not os.path.exists("pio_compile_here/MqttConnector"):
    os.makedirs("pio_compile_here/MqttConnector")

for file in glob.iglob('src/*.*'):
    print 'Copied file %s' % (file)
    shutil.copy2(file, "pio_compile_here/MqttConnector")
