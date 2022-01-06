[app]

# (str) Title of your application
title = Notes

# (str) Package name
package.name = notes

# (str) Package domain (needed for android/ios packaging)
package.domain = org.IdiotiePatence

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,html,css,db,js

# (str) Application versioning (method 1)
version = 0.0.6

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,flask,peewee

android.presplash_color = white
# (str) Presplash of the application
presplash.filename = %(source.dir)s/screen.png

# (str) Icon of the application
icon.filename = %(source.dir)s/ico.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 28

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path = ~/Android/Sdk

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop


# (str) Bootstrap to use for android builds
p4a.bootstrap = webview

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
p4a.port = 8080


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
