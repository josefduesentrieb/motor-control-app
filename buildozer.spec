[app]

title = MotorControlApp
package.name = motorcontrol
package.domain = org.example

source.dir = .
version = 0.1
entrypoint = main.py

requirements = python3,kivy,requests

fullscreen = 1
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.ndk_api = 21

android.entrypoint = org.kivy.android.PythonActivity
android.theme = '@android:style/Theme.NoTitleBar'

copy_libraries = 1
