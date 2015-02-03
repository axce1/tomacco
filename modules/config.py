import os.path
import subprocess
import configparser


path = 'tomatotimer.conf'


def create_conf():
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "ttime", "25")
    config.set("Settings", "lpause", "5")
    config.set("Settings", "spause", "3")

    with open(path, "w") as config_file:
        config.write(config_file)


def open_conf():
    if not os.path.exists(path):
        create_conf()

    conf_file = configparser.ConfigParser()
    conf_file.read(path)

    return conf_file


def read_conf(section, option):
    config = open_conf()

    value = config.get(section, option)

    return int(value)


def write_conf(section, option, value):
    config = open_conf()

    config.set(section, option, str(value))
    with open(path, "w") as config_file:
        config.write(config_file)


def notify(body):
        image = os.path.abspath('images/red-tomat.png')
        cmd=['notify-send', '--icon=%s' % image]
        cmd.extend(['TomatoTimer', body.encode('utf-8')])
        subprocess.call(cmd, stderr = open('/dev/null', 'a'))
