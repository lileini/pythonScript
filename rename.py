#文件重命名脚本，基于python3


import os
import functools
import re

preName = "100-50_"
newPreName = "end_"
path = r'I:\svn\长安\75A121\Doc\09 UIUE\仪表\动效\S202MCA动效\赛道模式\赛道模式上下坡视频序列帧\赛道0-100过渡循环序列_220719\赛道0-100过渡循环序列_220719\4-1.100-50过渡序列'
newSubNumberCount = 3
isReIndex = 1


def getIndex(x: str):
    if len(preName) == 0 :
        return int(re.findall(r'(.+?).png', x)[0])
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


old_dir = os.listdir(path)
print("原始目录为 %s" % old_dir)
old_dir.sort(key=functools.cmp_to_key(cmp))
# 重命名
index = 0
for i in old_dir:
    if not i.endswith('.png'):
        continue
    if isReIndex:
        new_name = '%s%s.png' % (newPreName, str(index).rjust(newSubNumberCount, '0'))
    else:
        new_name = '%s%s.png' % (newPreName, str(getIndex(i)).rjust(newSubNumberCount, '0'))
    index += 1
    os.rename(path + "/" + i, path + "/" + new_name)
new_dir = os.listdir(path)
print("现在的目录为%s" % new_dir)

# 删除多余的
# for i in old_dir:
#     if getIndex(i) % 2 > 0:
#         os.remove(path + "/" + i)
