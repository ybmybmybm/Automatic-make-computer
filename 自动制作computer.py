import os
# 这个程序可以帮助你配电脑
# 预算如果是4700,就转化成4000~5000,以此类推
"""
作者:@myb1myb3
Create by @myb1myb3
版本:1.0.2
Version:1.0.2
编写的软件:Visual Studio
Written software:Visual Studio
"""

VERSION = "1.0.2"

# 下面为配置
intel10002000 = "入门级\n\
处理器:Intel 赛扬G4900\n\
主板:昂达H110C+\n\
内存:玖合DDR3 1333 4GB\n\
HDD:西部数据蓝盘 500GB 16M SATA 笔记本硬盘(WD5000LPCX)\n\
SSD:大华C800 128GB SATA SSD\n\
显卡:核显\n\
机箱:金达灵剑(黑色)\n\
电源:金河田智能芯480GT电源\n\
显示器:AOC SWX01\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放 四方形便携迷你低音炮 黑色有线版\n\
散热器:大水牛两极风F08\n\
声卡:创意达蓝调PCI-E SB0060\n\
1831元"
amd10002000 = "入门级\n\
处理器:AMD Ryzen 3 1300X\n\
主板:影驰A320M 龙将 Ver1.0\n\
内存:玖合DDR3 1333 4GB\n\
HDD:西部数据蓝盘 500GB 16M SATA 笔记本硬盘(WD5000LPCX)\n\
SSD:大华C800 128GB SATA SSD\n\
显卡:盈通 R5 230-1G D3 VD\n\
机箱:金达灵剑(黑色)\n\
电源:金河田智能芯480GT电源\n\
显示器:AOC SWX01\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放 四方形便携迷你低音炮 黑色有线版\n\
散热器:大水牛两极风F08\n\
声卡:创意达蓝调PCI-E SB0060\n\
1990元"
intel20003000 = "低端\n\
处理器:Intel 酷睿i3 7100\n\
主板:昂达H110C+\n\
内存:酷兽DDR4 2133 8GB\n\
HDD:西部数据蓝盘 500GB 16M SATA 笔记本硬盘(WD5000LPCX)\n\
SSD:酷兽高速升级版 240GB SATA3 SSD\n\
显卡:铭瑄MS-GT710 重锤II\n\
机箱:金达灵剑(黑色)\n\
电源:台达VX270\n\
显示器:HSO E22EL\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放 四方形便携迷你低音炮 黑色有线版\n\
散热器:爱国者X3彩虹光\n\
声卡:创意达蓝调PCI-E SB0060\n\
2810元"
amd20003000 = "低端\n\
处理器:AMD Ryzen 5 1400\n\
主板:影驰A320M 龙将 Ver1.0\n\
内存:玖合精英 DDR4 2133 8GB\n\
HDD:HGST(原日立)Travelstar Z5K1000 750GB SATA3 32M\n\
SSD:酷兽高速升级版 240GB SATA3 SSD\n\
显卡:小影霸R7 430 2G\n\
机箱:金达灵剑(黑色)\n\
电源:长城PRIME450\n\
显示器:东星E926\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放807蓝色\n\
散热器:超频三 旋风F-72\n\
声卡:创意达蓝调PCI-E SB0060\n\
2959元"
intel30004000 = "主流\n\
处理器:Intel酷睿i3-7350K\n\
主板:昂达H110C全固版\n\
内存:酷兽DDR4 2133 8GB\n\
HDD:西部数据蓝盘 500GB 16M SATA 笔记本硬盘(WD5000LPCX)\n\
SSD:三星970 EVO 250GB NVMe M.2 SSD\n\
显卡:影驰GTX 1050 Ti 大将\n\
机箱:金达灵剑(黑色)\n\
电源:台达VX270\n\
显示器:HSO E22EL\n\
键鼠套装:现代HY-MA75W\n\
音箱:现代HY-66T黑\n\
散热器:酷冷至尊T20\n\
声卡:创意达蓝调KX-3传奇版\n\
3914元"
amd30004000 = "主流\n\
处理器:AMD Ryzen 5 3500X\n\
主板:技嘉H310M-H\n\
内存:金士顿DDR4 2400 8G\n\
HDD:HGST(原日立)Travelstar Z5K1000 750GB SATA3 32M\n\
SSD:三星860 EVO 250GB SATA SSD\n\
显卡:盈通RX 550-4G LP D5\n\
机箱:金达灵剑(黑色)\n\
电源:长城PRIME450\n\
显示器:东星E926\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放807蓝色\n\
散热器:酷冷至尊T20\n\
声卡:创意达蓝调PCI-E SN0105\n\
3998元"
intel40005000 = "主流\n\
处理器:Intel酷睿i5 9400F\n\
主板:华擎A320M-HDV\n\
内存:酷兽DDR4 2400 8GB\n\
HDD:西部数据蓝盘 1TB 64M SATA3 硬盘(WD10EZEX)\n\
SSD:三星970 EVO 500GB NVMe M.2 SSD\n\
显卡:影驰GeForce GTX 1650 骁将\n\
机箱:撒哈拉神光7号\n\
电源:航嘉JUMPER 300S\n\
显示器:HSO E22EL\n\
键鼠套装:现代HY-MA75W\n\
音箱:现代HY-66T黑\n\
散热器:酷冷至尊T20\n\
声卡:创意达蓝调R6\n\
4876元"
amd40005000 = "主流\n\
处理器:AMD Ryzen 5 3600\n\
主板:技嘉H310M-H\n\
内存:美商海盗船复仇者RGB PRO DDR4 3200 16GB\n\
HDD:HGST(原日立)Travelstar Z5K1000 750GB SATA3 32M\n\
SSD:三星970 EVO 250GB NVMe M.2 SSD\n\
显卡:盈通RX 550-4G LP D5\n\
机箱:金达灵剑(黑色)\n\
电源:长城PRIME450\n\
显示器:东星E926\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放807蓝色\n\
散热器:酷冷至尊T20\n\
声卡:创意达蓝调PCI-E SN0105\n\
4898元"
intel50007000 = "中高端\n\
处理器:Intel 酷睿i7 9700\n\
主板:七彩虹H410M-K PRO V20\n\
内存:酷兽DDR4 2400 8GB\n\
HDD:西部数据蓝盘 1TB 64M SATA3 硬盘(WD10EZEX)\n\
SSD:三星970 EVO 500GB NVMe M.2 SSD\n\
显卡:技嘉GeForce GTX 1650 SUPER OC 4G\n\
机箱:撒哈拉神光7号\n\
电源:长城PRIME450\n\
显示器:HSO E22EL\n\
键鼠套装:现代HY-MA75W\n\
音箱:现代HY-66T黑\n\
散热器:酷冷至尊T20\n\
声卡:创意达蓝调R6\n\
6986元"
amd50007000 = "中高端\n\
处理器:AMD R7 3700X\n\
主板:华硕PRIME B460M-K\n\
内存:美商海盗船复仇者RGB PRO DDR4 3200 16GB\n\
HDD:HGST(原日立)Travelstar Z5K1000 750GB SATA3 32M\n\
SSD:三星970 EVO 250GB NVMe M.2 SSD\n\
显卡:蓝宝石RX580 2048SP 8G D5 白金版 OC\n\
机箱:金达灵剑(黑色)\n\
电源:长城PRIME450\n\
显示器:东星E926\n\
键鼠套装:现代HY-MA75W\n\
音箱:乐放807蓝色\n\
散热器:酷冷至尊T20\n\
声卡:创意达蓝调PCI-E SN0105\n\
6917元"
intel700010000 = "高端\n\
处理器:Intel 酷睿i7 8086k\n\
主板:七彩虹H410M-K PRO V20\n\
内存:美商海盗船复仇者RGB PRO DDR4 3200 16GB\n\
HDD:西部数据蓝盘 1TB 64M SATA3 硬盘(WD10EZEX)\n\
SSD:三星970 EVO 500GB NVMe M.2 SSD\n\
显卡:翔升GeForce RTX 2060 战神 6G D6\n\
机箱:航嘉GX680H时光\n\
电源:大水牛劲强500\n\
显示器:HSO E22EL\n\
键鼠套装:现代HY-MA75W\n\
音箱:现代HY-66T黑\n\
散热器:利民银箭Arrow IB-E 超频版\n\
声卡:创意达蓝调R6\n\
9875元"
amd700010000 = "高端\n\
处理器:AMD Ryzen 9 3900X\n\
主板:华硕PRIME B460M-K\n\
内存:美商海盗船复仇者RGB PRO DDR4 3200 16GB\n\
HDD:HGST(原日立)Travelstar Z5K1000 750GB SATA3 32M\n\
SSD:三星970 EVO 250GB NVMe M.2 SSD\n\
显卡:撼讯RX 5700 竞技版\n\
机箱:撒哈拉神光7号\n\
电源:长城PRIME450\n\
显示器:微星E2209\n\
键鼠套装:现代HY-MA75W\n\
音箱:现代HY-66T黑\n\
散热器:超频三东海X6\n\
声卡:创意达蓝调PCI-E SN0105\n\
9625元"
intel1000020000 = "旗舰\n\
处理器:Intel酷睿 i9 10900K\n\
主板:华硕TUF B360M-PLUS GAMING\n\
内存:金士顿骇客神条 Predator DDR4 3200 32GB(16G×2)\n\
HDD:西部数据SE 2TB 7200转 64MB SATA3企业级\n\
SSD:金泰克P500 512GB NVMe M.2 SSD\n\
显卡:小影霸RTX 2080TI 11G 涡轮\n\
机箱:航嘉GX680H时光\n\
电源:大水牛劲强500\n\
显示器:AOC 27G2\n\
键鼠套装:罗技MK120键鼠套装\n\
音箱:小米AI音箱\n\
散热器:利民银箭Arrow IB-E 超频版\n\
声卡:创新Sound Blaster Z 声卡\n\
19927元"
amd1000020000 = "旗舰\n\
处理器:AMD Ryzen 9 3950X\n\
主板:华硕PRIME B460M-K\n\
内存:美商海盗船复仇者RGB PRO DDR4 3200 16GB\n\
HDD:HGST(原日立)Travelstar Z5K1000 750GB SATA3 32M\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD\n\
显卡:撼讯RX 5700 竞技版\n\
机箱:大水牛铁血战士\n\
电源:长城PRIME450\n\
显示器:微星E2209\n\
键鼠套装:罗技MK120键鼠套装\n\
音箱:飞利浦SPA520S\n\
散热器:九州风神大霜塔\n\
声卡:创新Sound Blaster Z 声卡\n\
19968元"
intel2000050000 = "发烧\n\
处理器:Intel酷睿 i9 9980XE\n\
主板:华硕PRIME Z390-P\n\
内存:芝奇RGB 皇家戟 DDR4 3200 64GB(16GB×4)\n\
HDD:西部数据14TB 7200转 512MB 金盘(WD141VRYZ)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD\n\
显卡:微星GeForce RTX 2080 Ti VENTUS 11G OC 万图师\n\
机箱:华硕 ROG Strix Helios 太阳神\n\
电源:全汉Hydro PTM+\n\
显示器:三星S34J550WQC\n\
键鼠套装:雷柏8050T多模式无线键鼠套装\n\
音箱:小米AI音箱\n\
散热器:九州风神堡垒360EX RGB\n\
声卡:创新Sound Blaster Z 声卡\n\
48067元"
amd2000050000 = "发烧\n\
处理器:AMD Ryzen Threadripper 3960X\n\
主板:华硕ROG CROSSHAIR VI EXTREME\n\
内存:芝奇RGB 皇家戟 DDR4 3600 64GB(16GB×4)\n\
HDD:东芝12TB 7200转 256MB(MG07ACA12TE)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD\n\
显卡:撼讯RX 5700XT LIQUID DEVIL毒液\n\
机箱:华硕 ROG Strix Helios \n\
电源:全汉Hydro PTM+\n\
显示器:三星S34J550WQC\n\
键鼠套装:戴尔KM636\n\
音箱:小米AI音箱\n\
散热器:Coollion波浪BMR A-1\n\
声卡:创新Sound Blaster Z 声卡\n\
47265元"
intel50000100000 = "顶级\n\
处理器:Intel酷睿 i9 9980XE\n\
主板:技嘉X299X AORUS XTREME\n\
内存:芝奇RGB 皇家戟 DDR4 3200 64GB(16GB×4)(x2)\n\
HDD:西部数据14TB 7200转 512MB 金盘(WD141VRYZ)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD\n\
显卡:华硕ROG Matrix GeForce RTX 2080 Ti\n\
机箱:华硕 ROG Strix Helios 太阳神\n\
电源:全汉Hydro PTM+\n\
显示器:三星S34J550WQC\n\
键鼠套装:雷柏8050T多模式无线键鼠套装\n\
音箱:小米AI音箱\n\
散热器:九州风神堡垒360EX RGB\n\
声卡:创新Sound Blaster Z 声卡\n\
90968元"
amd50000100000 = "顶级\n\
处理器:AMD Ryzen Threadripper 3990X\n\
主板:微星PRESTIGE X570 CREATION创世板\n\
内存:芝奇RGB 皇家戟 DDR4 3600 64GB(16GB×4)(x2)\n\
HDD:东芝12TB 7200转 256MB(MG07ACA12TE)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD(x2)\n\
显卡:撼讯RX 5700XT LIQUID DEVIL毒液(x2)\n\
机箱:华硕 ROG Strix Helios \n\
电源:全汉Hydro PTM+\n\
显示器:优派VP3881\n\
键鼠套装:戴尔KM636\n\
音箱:小米AI音箱\n\
散热器:Coollion波浪BMR A-1\n\
声卡:创新Sound Blaster Z 声卡\n\
93740元"
intel100000200000 = "顶级\n\
处理器:Intel酷睿 i9 9980XE\n\
主板:技嘉X299X AORUS XTREME\n\
内存:芝奇RGB 皇家戟 DDR4 3600 256GB(32GB×8)\n\
HDD:西部数据14TB 7200转 512MB 金盘(WD141VRYZ)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD(x2)\n\
显卡:华硕ROG Matrix GeForce RTX 2080 Ti(x2)\n\
机箱:华硕 ROG Strix Helios 太阳神\n\
电源:全汉Hydro PTM+\n\
显示器:戴尔UP3218K\n\
键鼠套装:雷柏8050T多模式无线键鼠套装\n\
音箱:哈曼卡顿SABRE SB35\n\
散热器:九州风神堡垒360EX RGB\n\
声卡:华硕 EONE MKII MUSES\n\
193818元"
amd100000200000 = "顶级\n\
处理器:AMD Ryzen Threadripper 3990X\n\
主板:微星PRESTIGE X570 CREATION创世板\n\
内存:芝奇RGB 皇家戟 DDR4 3600 256GB(32GB×8)\n\
HDD:东芝12TB 7200转 256MB(MG07ACA12TE)(x2)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD(x2)\n\
显卡:撼讯RX 5700XT LIQUID DEVIL毒液(x2)\n\
机箱:Tt Level 20\n\
电源:全汉Hydro PTM+\n\
显示器:艺卓ColorEdge CG319X\n\
键鼠套装:雷蛇粉晶游戏套装\n\
音箱:小米AI音箱\n\
散热器:Coollion波浪BMR A-1\n\
声卡:华硕 EONE MKII MUSES\n\
156551元"
intel200000500000 = "豪华\n\
处理器:Intel酷睿 i9 9980XE\n\
主板:技嘉X299X AORUS XTREME\n\
内存:芝奇RGB 皇家戟 DDR4 3600 256GB(32GB×8)\n\
HDD:西部数据14TB 7200转 512MB 金盘(WD141VRYZ)(x2)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD(x2)\n\
显卡:华硕ROG Matrix GeForce RTX 2080 Ti(x2)\n\
机箱:Tt Level 20\n\
电源:全汉Hydro PTM+\n\
显示器:AOC 98U1\n\
键鼠套装:雷蛇粉晶游戏套装\n\
音箱:达尼RUBICON 6黑色\n\
散热器:九州风神堡垒360EX RGB\n\
声卡:华硕 EONE MKII MUSES\n\
383400元"
amd200000500000 = "豪华\n\
处理器:AMD Ryzen Threadripper 3990X\n\
主板:微星PRESTIGE X570 CREATION创世板\n\
内存:芝奇RGB 皇家戟 DDR4 3600 256GB(32GB×8)\n\
HDD:西部数据14TB 7200转 512MB 金盘(WD141VRYZ)(x2)\n\
SSD:三星970 PRO 512GB NVMe M.2 SSD(x2)\n\
显卡:撼讯RX 5700XT LIQUID DEVIL毒液(x2)\n\
机箱:Tt Level 20\n\
电源:全汉Hydro PTM+\n\
显示器:AOC 98U1\n\
键鼠套装:雷蛇粉晶游戏套装\n\
音箱:达尼RUBICON 6黑色\n\
散热器:Coollion波浪BMR A-1\n\
声卡:华硕 EONE MKII MUSES\n\
338276元"

# 下面是程序部分
def program(pinpai,yusuan):
    yusuan = int(yusuan)
    print(yusuan)
    if pinpai == "in":
        if yusuan >= 2000 and yusuan < 3000:
            print(intel10002000)
        elif yusuan >= 3000 and yusuan < 4000:
            print(intel20003000)
        elif yusuan >= 4000 and yusuan < 5000:
            print(intel30004000)
        elif yusuan >= 5000 and yusuan < 7000:
            print(intel40005000)
        elif yusuan >= 7000 and yusuan < 10000:
            print(intel50007000)
        elif yusuan >= 10000 and yusuan < 20000:
            print(intel700010000)
        elif yusuan >= 20000 and yusuan < 50000:
            print(intel1000020000)
        elif yusuan >= 50000 and yusuan < 100000:
            print(intel2000050000)
        elif yusuan >= 100000 and yusuan < 200000:
            print(intel50000100000)
        elif yusuan >= 200000 and yusuan < 500000:
            print(intel100000200000)
        elif yusuan >= 500000:
            print(intel200000500000)
    if pinpai == "3a":
        if yusuan >= 2000 and yusuan < 3000:
            print(amd10002000)
        elif yusuan >= 3000 and yusuan < 4000:
            print(amd20003000)
        elif yusuan >= 4000 and yusuan < 5000:
            print(amd30004000)
        elif yusuan >= 5000 and yusuan < 7000:
            print(amd40005000)
        elif yusuan >= 7000 and yusuan < 10000:
            print(amd50007000)
        elif yusuan >= 10000 and yusuan < 20000:
            print(amd700010000)
        elif yusuan >= 20000 and yusuan < 50000:
            print(amd1000020000)
        elif yusuan >= 50000 and yusuan < 100000:
            print(amd2000050000)
        elif yusuan >= 100000 and yusuan < 200000:
            print(amd50000100000)
        elif yusuan >= 200000 and yusuan < 500000:
            print(amd100000200000)
        elif yusuan >= 500000:
            print(amd200000500000)

def main():
    temp = input("你要配amd还是intel?")
    ys = input("预算:")
    ys = int(ys)
    if temp == "amd":
        program("3a",ys)
    if temp == "intel":
        program("in",ys)

if __name__ == '__main__':
    main()

    os.system("pause")
