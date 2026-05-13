[app]
title = Mi Alerta Munoz
package.name = alertamunoz
package.domain = org.damian
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# --- Android specific ---
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True

# Permisos para tu app de alertas (Ajustar según necesites)
android.permissions = INTERNET, SEND_SMS, ACCESS_FINE_LOCATION

# --- Python for android ---
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
