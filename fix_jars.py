import os, zipfile, shutil, subprocess

base = r"C:\Users\kaibo\Downloads\portfollio"
build = os.path.join(base, "build")

# Clean build directory
if os.path.exists(build): shutil.rmtree(build)
os.makedirs(build)

# Copy the build from the Python script output
src = r"C:\Users\kaibo\Downloads\portfollio\src2"

# Create the build structure
pkg_dirs = ["org/bukkit/command", "org/bukkit/entity", "org/bukkit/event",
            "org/bukkit/event/player", "org/bukkit/inventory",
            "org/bukkit/configuration/file", "org/bukkit/scoreboard",
            "org/bukkit/plugin/java", "me/kaibo/tpasystem", "me/kaibo/chatmanager"]
for sub in pkg_dirs:
    os.makedirs(os.path.join(build, *sub.split("/")), exist_ok=True)

# Create plugin.yml at root
with open(os.path.join(build, "plugin.yml"), 'w') as f:
    f.write("name: TpaSystem\nversion: 1.0.0\nmain: me.kaibo.tpasystem.TpaSystem\napi-version: 1.20\nauthor: Sharky\n")

# Create paper-plugin.yml at root (Paper 1.21+ format)
with open(os.path.join(build, "paper-plugin.yml"), 'w') as f:
    f.write("name: TpaSystem\nversion: 1.0.0\nmain: me.kaibo.tpasystem.TpaSystem\napi-version: 1.21\nauthor: Sharky\ndescription: Teleport request system\n")

# Create messages.yml
os.makedirs(os.path.join(build, "me/kaibo/tpasystem/messages"), exist_ok=True)
with open(os.path.join(build, "me/kaibo/tpasystem/messages/messages.yml"), 'w') as f:
    f.write("messages:\n  loaded: '&aPlugin loaded'\n")

# Create MANIFEST.MF
os.makedirs(os.path.join(build, "META-INF"), exist_ok=True)
with open(os.path.join(build, "META-INF/MANIFEST.MF"), 'w') as f:
    f.write("Manifest-Version: 1.0\nMain-Class: me.kaibo.tpasystem.TpaSystem\n\n")

# Build JAR using Python zipfile for precise control
jar_path = os.path.join(base, "TpaSystem.jar")
with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(build):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, build)
            zf.write(filepath, arcname)

print(f"Created: {jar_path} ({os.path.getsize(jar_path)} bytes)")

# Verify
with zipfile.ZipFile(jar_path) as zf:
    names = zf.namelist()
    print(f"paper-plugin.yml at root: {'paper-plugin.yml' in names}")
    print(f"plugin.yml at root: {'plugin.yml' in names}")
    print(f"MANIFEST.MF: {'META-INF/MANIFEST.MF' in names}")

# Same for ChatManager
build2 = os.path.join(base, "build2")
if os.path.exists(build2): shutil.rmtree(build2)
os.makedirs(build2)

for sub in pkg_dirs:
    os.makedirs(os.path.join(build2, *sub.split("/")), exist_ok=True)

with open(os.path.join(build2, "plugin.yml"), 'w') as f:
    f.write("name: ChatManager\nversion: 1.0.0\nmain: me.kaibo.chatmanager.ChatManager\napi-version: 1.20\nauthor: Sharky\n")

with open(os.path.join(build2, "paper-plugin.yml"), 'w') as f:
    f.write("name: ChatManager\nversion: 1.0.0\nmain: me.kaibo.chatmanager.ChatManager\napi-version: 1.21\nauthor: Sharky\ndescription: Advanced chat management\n")

os.makedirs(os.path.join(build2, "me/kaibo/chatmanager/messages"), exist_ok=True)
with open(os.path.join(build2, "me/kaibo/chatmanager/messages/messages.yml"), 'w') as f:
    f.write("messages:\n  loaded: '&aPlugin loaded'\n")

os.makedirs(os.path.join(build2, "META-INF"), exist_ok=True)
with open(os.path.join(build2, "META-INF/MANIFEST.MF"), 'w') as f:
    f.write("Manifest-Version: 1.0\nMain-Class: me.kaibo.chatmanager.ChatManager\n\n")

jar_path2 = os.path.join(base, "ChatManager.jar")
with zipfile.ZipFile(jar_path2, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(build2):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, build2)
            zf.write(filepath, arcname)

print(f"Created: {jar_path2} ({os.path.getsize(jar_path2)} bytes)")
print("Done!")
