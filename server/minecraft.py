import os
import signal
import subprocess


class MinecraftServer:
    def __init__(self):
        self.process = None

    def start(self):
        command = "java -Xmx1024M -Xms1024M -jar fabric.jar nogui"
        self.process = subprocess.Popen(command.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd='minecraft')

    def stop(self):
        if self.process:
            os.kill(self.process.pid, signal.SIGTERM)
            self.process = None
