[app]
title = Alerta Munoz
package.name = alertamunoz
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1
requirements = python3,kivy==2.2.1
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1