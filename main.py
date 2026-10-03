import minecraft_launcher_lib as mll
import subprocess

path = mll.utils.get_minecraft_directory()
version = "1.16.5"
nickname = "Steve"

print(f"Установка версии {version}...")
mll.install.install_minecraft_version(versionid=version, minecraft_directory=path)

options = {
    "username": nickname,
    "uuid": "",
    "token": "",
}

command = mll.command.get_minecraft_command(
    version=version,
    minecraft_directory=path,
    options=options
)

print("Запуск Minecraft...")
subprocess.run(command)
