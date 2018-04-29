"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/12 16:48
"""


def init():
    """
    批量更新所有包
    :return:
    """
    import pip
    from subprocess import call

    for dist in pip.get_installed_distributions():
        call("pip3 install --upgrade " + dist.project_name, shell=True)


if __name__ == "__main__":
    init()
