import scapy
from scapy.all import *

p=IP(dst='192.168.0.1')/TCP(dport=(1,60))/"5052078 240447 7565178 920292 1473661 6436764 8802248 9554213 737618 8110929 4374656 3157228 232260 239812 2690551 2698746 3673430 7054957 4556368 177456 5005782 8762343 6952575 1930326 1603766 3311769 8764256 9126212 7640455 2023221 6075132 5470078 223936 5826061 124874 5390648 3077096 6882966 4608162 677985 7524020 4070847 4124236 5522894 4301882 9290151 6441449 7040621 7147164 1443883 1979425 4119709 1416937 5210220 1042713 9118907 4224840 5653762 8636747 9309042 8824566 2531453 7215066 5095048 5088788 2549324 6569355 6565565 8364248 8127160 5529024 4951645 8079476 5657465 7151589 2625377 6545216 5871513 7383136 9962797 3641502 7416221 862069 360952 8765638 6546658 7098341 8815971 9556848 3912539 2590477 2332696 3437887 8585078 3633774 3510662 3221356 6702811 1258321 1605310 4076264 2053262 4537020 4970829 3998686 8195003 6552771 890984 5428683 2896626 4407684 5446327 1469884 9412015 6194797 3790338 284107 573783 8942407 1731792 8941666 8026871 2743983 9856692 3120689 3371761 9135561 9958717 3241660 8222021 9830311 3581969 8734090 155008 7590427 5955583 7729818 8834745 3411943 1732429 2901024 5055451 7105368 7679576 7626720 3787755 6664449 8834816 5190691 3299996 9899730 4871835 9032636 2873237 5395868 4377549 7622149 9690567 5863391 7042507 2306842 4455365 6997603 9288898 4173125 5510207 5870117 403136 5714122 434298 4566385 8228327 9971360 6456186 724989 4966403 1868844 4196215 6307160 4398801 6296741 3506309 2562489 8965517 515262 6339698 7972625 1827654 8247874 6912667 9812156 2167542 7674444 1966878 8496959 4509409 8969226 6614566 2618748 6312739 8296988 4662309 4722217 2422555 2729332 6602245 1014222 8865113 5248864 4162705 6464503 8896282 6104526 4418700 2493113 5516567 5539694 5972151 569107 2655302 715225 6146798 3797234 105236 7142182 9483299 1396419 2309152 3999140 5592080 3927822 4314343 1594598 5122449 3377367 8028376 1612895 9569134 163992 3523 7664922 4357273 6242939 4498442 8796169 547559 5135029 4992208 8723130 2353705 8482097 560847 4262881 4286652 3140704 3445971 5698120 4683253 9375419 4226945 237985 9965679 6847026 7776135"
print(p.show())
wrpcap("packet.pcap",p)