#!/usr/bin/python 
# -*- coding: utf-8 -*- 

from optparse import OptionParser
from optparse import OptionGroup
import sys

usage = 'Usage: %prog [options] arg1 arg2 ...'

parser = OptionParser(usage,version='%prog 1.0')
#通过OptionParser类创建parser实例,初始参数usage中的%prog等同于os.path.basename(sys.argv[0]),即
#你当前所运行的脚本的名字，version参数用来显示当前脚本的版本。

'''
添加参数，-f、--file是长短options，有一即可。

action用来表示将option后面的值如何处理，比如:
XXX.py -f test.txt
经过parser.parse_args()处理后,则将test.txt这个值存储进-f所代表的一个对象，即定义-f中的dest
即option.filename = 'test.txt'
action的常用选项还有store_true,store_false等，这两个通常在布尔值的选项中使用。

metavar仅在显示帮助中有用，如在显示帮助时会有：
-f FILE, --filename=FILE    write output to FILE
-m MODE, --mode=MODE  interaction mode: novice, intermediate, or expert
                        [default: intermediate]
如果-f这一项没有metavr参数，则在上面会显示为-f FILENAME --filename=FILENAME,即会显示dest的值

defalut是某一选项的默认值，当调用脚本时，参数没有指定值时，即采用default的默认值。
'''

parser.add_option('-f','--file',
                  action='store',dest='filename',
                  metavar='FILE',help='write output to FILE')

parser.add_option('-m','--mode',
                  default = 'intermediate',
                  help='interaction mode:novice,intermediate,or expert [default:%default]')
parser.add_option('-v','--verbose',
                  action='store_true',dest='verbose',default=True,
                  help='make lots of noise [default]')

parser.add_option('-q','--quiet',
                  action='store_false',dest='verbose',
                  help="be vewwy quiet (I'm hunting wabbits)")

group = OptionGroup(parser,'Dangerous Options',
                    'Caution: use these options at your own risk.'
                    'It is believed that some of them bite.')
#调用OptionGroup类，定制以组显示的option

group.add_option('-g',action='store_true',help='Group option.')
#添加option
parser.add_option_group(group)
#将刚定制的groupoption加入parser中

group = OptionGroup(parser,'Debug Options')
group.add_option('-d','--debug',action='store_true',
                 help='Print debug information.')
group.add_option('-s','--sql',action='store_true',
                 help='Print all SQL statements executed')
group.add_option('-e',action='store_true',help='Print every action done')
parser.add_option_group(group)

(options,args) = parser.parse_args(sys.argv)
print options.verbose
if options.filename:
	print options.filename
#解析脚本输入的参数值，options是一个包含了option值的对象
#args是一个位置参数的列表