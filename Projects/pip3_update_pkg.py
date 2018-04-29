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
    import pip3
    from subprocess import call

    for dist in pip3.get_installed_distributions(local_only=False):
        call("pip3 install --upgrade " + dist.project_name, shell=True)


if __name__ == "__main__":
    init()
