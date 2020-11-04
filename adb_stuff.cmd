adb.exe reverse --remove-all

adb.exe forward --remove-all
echo "Done removing"
adb.exe push scrcpy-server /data/local/tmp/scrcpy-server.jar
adb.exe reverse localabstract:scrcpy tcp:27183
echo "Done setting up"
:: adb.exe shell CLASSPATH=/data/local/tmp/scrcpy-server.jar app_process / com.genymobile.scrcpy.Server 1.12.1 1024 8000000 0 false - false false
adb.exe shell CLASSPATH=/data/local/tmp/scrcpy-server.jar app_process / com.genymobile.scrcpy.Server 1.12.1 1024 2000000 0 false - true true
echo "Done"
