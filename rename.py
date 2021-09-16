#文件重命名脚本，基于python3


import os
import functools
import re

preName = "up_"
path = r'D:\noboPic\运动模式序列置修改_水温表遮挡\运动模式表盘起来修改'


def getIndex(x: str):
    return int(re.findall(r'%s(.+?).png' % preName, x)[0])


def cmp(x: str, y: str):
    a = getIndex(x)
    b = getIndex(y)
    print("x=%d,y=%d" % (a, b))
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


old_dir = os.listdir(path)  # 获取/home/linuxidc/linuxidc.com目录下的所有文件目录
print("原始目录为 %s" % old_dir)
old_dir.sort(key=functools.cmp_to_key(cmp))
# 重命名
# for i in old_dir:
#     if not i.endswith('.png'):
#         continue
#     new_name = '%s%s.png' % (preName, str(getIndex(i)).rjust(5, '0'))
#     os.rename(path + "/" + i, path + "/" + new_name)
# new_dir = os.listdir(path)
# print("现在的目录为%s" % new_dir)

# 删除多余的
for i in old_dir:
    if getIndex(i) % 2 > 0:
        os.remove(path + "/" + i)
