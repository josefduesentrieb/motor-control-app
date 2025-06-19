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
android.build_tools_version = 33.0.2

android.entrypoint = org.kivy.android.PythonActivity
android.theme = '@android:style/Theme.NoTitleBar'

copy_libraries = 1

[environment]
ANDROIDSDK = %(ANDROID_SDK_ROOT)s
ANDROIDNDK = %(ANDROID_SDK_ROOT)s/ndk/23.1.7779620
ANDROIDAPI = 33
ANDROIDMINAPI = 21
