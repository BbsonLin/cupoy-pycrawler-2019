D29：Scrapy 爬蟲流程 (4) - 多網頁爬蟲
=====

Code
-----
[commit](https://github.com/BbsonLin/cupoy-pycrawler-2019/commit/3a52a10877754233d0f5ca80c0e9bc374d237163#diff-ed5b6890b86f8d9776fe21cf46a6b376)

Output
-----

[crawled_data](https://github.com/BbsonLin/cupoy-pycrawler-2019/blob/master/myproject/crawled_data/20200210T163655-20200210T163656.json)

```
PS E:\Code\dev-projects\Cupoy\pycrawler\myproject> scrapy crawl ptt_board_crawler -a board="Gossiping"
2020-02-10 16:59:59 [scrapy.utils.log] INFO: Scrapy 1.8.0 started (bot: myproject)
2020-02-10 16:59:59 [scrapy.utils.log] INFO: Versions: lxml 4.4.2.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 19.10.0, Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Windows-10-10.0.18362-SP0
2020-02-10 16:59:59 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'myproject', 'EDITOR': 'D:\\Microsoft VS Code\\Code.exe', 'NEWSPIDER_MODULE': 'myproject.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['myproject.spiders']}
2020-02-10 16:59:59 [scrapy.extensions.telnet] INFO: Telnet Password: 548b166ecd596128
2020-02-10 16:59:59 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2020-02-10 17:00:00 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',    
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',      
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',    
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-02-10 17:00:00 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-02-10 17:00:00 [scrapy.middleware] INFO: Enabled item pipelines:
['myproject.pipelines.JSONPipline']
2020-02-10 17:00:00 [scrapy.core.engine] INFO: Spider opened
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Start: open_spider ...
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Create temp file for store JSON - E:\Code\dev-projects\Cupoy\pycrawler\myproject\crawled_data\.tmp.json.swp  
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: End: open_spider ...
2020-02-10 17:00:00 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-02-10 17:00:00 [scrapy.extensions.telnet] INFO: Telnet console listening 
on 127.0.0.1:6023
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.ptt.cc/robots.txt> (referer: None)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/index.html> (referer: None)
2020-02-10 17:00:00 [py.warnings] WARNING: E:\Code\dev-projects\Cupoy\pycrawler\myproject\myproject\spiders\ptt_board_crawler.py:25: UserWarning: No parser 
was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 25 of the file E:\Code\dev-projects\Cupoy\pycrawler\myproject\myproject\spiders\ptt_board_crawler.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.

  soup = BeautifulSoup(response.text)

2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324650.A.2A4.html Re: [新聞] 黃瀞瑩職缺傳內定？ 北市府:依法公告
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324701.A.27D.html Re: [問卦] 有哪些Youtuber你不退訂卻又
不太看的?
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324709.A.744.html [問卦] 有封城的八卦嗎?
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324711.A.FFD.html Re: [問卦] 把公主號上面的台灣人接回台
灣 你支持嗎
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324767.A.BF6.html [問卦] 有個嬉皮在我游泳池怎麼辦      
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324779.A.856.html [問卦]疫情嚴重 去對岸工作的怎麼辦？  
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324860.A.7A1.html [問卦] 台灣醫療以餐廳來比喻大概是什麼
等級？
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324879.A.3F7.html Re: [問卦] 之前看到chinese taipei就抓
狂的人 痊癒沒
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324891.A.EA8.html [問卦] 潛伏期傳染
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324929.A.791.html [問卦] 皰疹病毒，不會消失的八卦？    
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324943.A.DFB.html Re: [爆卦] 80台藝人集體錄影為武漢肺炎
祈禱發聲
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324967.A.037.html [問卦] 屍速列車2會找成龍來拍嗎       
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324975.A.75D.html [問卦] 屍速列車是怎麼把疫情控制住的  
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581324991.A.CB4.html Re: [問卦] 一芳新聞天天爆  皮件公司沒
新聞
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581325010.A.AD0.html [問卦] 是不是應該宣導全戴口罩比較好  
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581325012.A.8EA.html [問卦] 現在印度是不是人類最後生存指標

2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581325139.A.85F.html [問卦] 聽過最中二的一句話
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581325177.A.1D9.html Re: [問卦] 之前看到chinese taipei就抓
狂的人 痊癒沒
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Parse article: https://www.ptt.cc/bbs/Gossiping/M.1581325192.A.9B5.html Re: [問卦] 為什麼台灣拍不出寄生上流？

2020-02-10 17:00:00 [ptt_board_crawler] INFO: REACH LAST ARTICLE...
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324650.A.2A4.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324767.A.BF6.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324701.A.27D.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324711.A.FFD.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324709.A.744.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324779.A.856.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581325139.A.85F.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581325177.A.1D9.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [py.warnings] WARNING: E:\Code\dev-projects\Cupoy\pycrawler\myproject\myproject\spiders\ptt_board_crawler.py:53: UserWarning: No parser 
was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 53 of the file E:\Code\dev-projects\Cupoy\pycrawler\myproject\myproject\spiders\ptt_board_crawler.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.

  soup = BeautifulSoup(response.text)

2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:00 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324650.A.2A4.html>
{'id': 'M.1581324650.A.2A4', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324650.A.2A4.html', 'author': 'oldmangoes (喝一杯憂鬱的咖啡)', 'title': 'Re: [新
聞] 黃瀞瑩職缺傳內定？ 北市府:依法公告', 'date': 'Mon Feb 10 16:50:48 2020', 'content': '白綠合作時\n\n綠共：我柯就是公開透明\n\n白綠拆夥後\n\n綠共：你柯就 
是黑箱作業\n\n\n綠共雙標黨 雙標事件早已罄竹難書\n\n還一堆人挺\n\n笑死\n\n817萬
口支障的優質選擇\n\n\n\n最後告訴你啦\n\n機要人員就是政務官人事權\n\n完全沒有問
題 : 學姐離職: 柯屁眾叛親離留不住人才 : 學姐回鍋: 柯屁內定.酬庸 : 學姊薪水低: 
柯屁慣老闆.黑心.壓榨 : 學姊薪水高: 肥貓專業不足不值得領高薪 : 學姊帶職請假輔選
:違反行政中立違法 : 學姊辭職輔選: 選舉考量無恥 : 學姊職缺2/7截止?  不管2/10截 
止那個職缺才是 : 提前錄取柯屁吃屎柯糞吃屎 https://www.ptt.cc/bbs/Gossiping/M.1581324650.A.2A4.html 小小機要 跟 政務首長比？？？\n\n綠酬庸的都是大官\n\n你可 
以用自己人\n\n但是要用對人\n\n舉例：不是讓應該一個沒有交通專業的人當交通部長', 'comments': [{'push_tag': '噓', 'push_userid': 'a1277034', 'push_content': ' 
綠共雙標笑死三四五標啦', 'push_ipdatetime': '114.137.140.52 02/10 16:51'}, {'push_tag': '→', 'push_userid': 'nakayamayyt', 'push_content': '笑死人 當然沒問 
題啊 所以蚵CF蚵糞', 'push_ipdatetime': '114.25.131.105 02/10 16:52'}, {'push_tag': '→', 'push_userid': 'nakayamayyt', 'push_content': '整天嘴別人人事是在嘴 
什麼', 'push_ipdatetime': '114.25.131.105 02/10 16:52'}, {'push_tag': '推', 'push_userid': 'm21423', 'push_content': '笑死 當年一堆 1450寄生柯', 'push_ipdatetime': '115.82.8.64 02/10 16:53'}, {'push_tag': '噓', 'push_userid': 'lysimach', 'push_content': '墨綠兩岸一家親', 'push_ipdatetime': '180.204.197.30 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'peterw', 'push_content': '順風的 
時候都是同志，逆風的時候都是臥底', 'push_ipdatetime': '223.140.176.118 02/10 16:56'}, {'push_tag': '噓', 'push_userid': 'sumins', 'push_content': '柯糞專門 
洗種種文章誒 有夠可憐', 'push_ipdatetime': '180.217.125.116 02/10 16:56'}, {'push_tag': '噓', 'push_userid': 'sumins', 'push_content': '不管是九萬還六萬台派
跟你嘴幾篇就不想嘴', 'push_ipdatetime': '180.217.125.116 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'sumins', 'push_content': '了 柯糞以為一直洗能洗成 
白的 柯連啊', 'push_ipdatetime': '180.217.125.116 02/10 16:57'}, {'push_tag': 
'→', 'push_userid': 'nakayamayyt', 'push_content': '笑死人 這種邏輯就像講偷大 
錢才算', 'push_ipdatetime': '114.25.131.105 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'nakayamayyt', 'push_content': '小偷 偷小錢就不算小偷', 'push_ipdatetime': '114.25.131.105 02/10 16:58'}, {'push_tag': '噓', 'push_userid': 'lyleselena', 'push_content': '檳榔渣的廢文', 'push_ipdatetime': '39.9.222.62 02/10 16:59'}], 'comment_stats': {'all': 12, 'count': -3, 'push': 2, 'boo': 5, 'neutral': 5}}
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581325010.A.AD0.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324991.A.CB4.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581325012.A.8EA.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324767.A.BF6.html>
{'id': 'M.1581324767.A.BF6', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324767.A.BF6.html', 'author': 'Changyaya ()', 'title': '[問卦] 有個嬉皮在我游泳 
池怎麼辦', 'date': 'Mon Feb 10 16:52:45 2020', 'content': '安安\n大家好\n我在 
我的豪華游泳池聽歌啦\n突然有個滿臉是血的女的衝進來\n掉進游泳池\n一直尖叫又開槍
\n\n請問我該拿出我的秘密武器嗎\n求解\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324767.A.BF6.html', 'comments': [{'push_tag': '噓', 'push_userid': 'XperiaZ6C', 'push_content': '哪部', 'push_ipdatetime': '173.196.212.226 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': '哪部?', 'push_ipdatetime': '39.12.32.241 02/10 16:53'}, {'push_tag': '推', 'push_userid': 'kairi5217', 'push_content': '噴火槍啊', 'push_ipdatetime': '27.242.158.16 02/10 16:53'}, {'push_tag': '噓', 'push_userid': 'powyo', 'push_content': '哪部', 'push_ipdatetime': '118.163.229.98 02/10 16:53'}, {'push_tag': '噓', 'push_userid': 'ja1295', 'push_content': '哪部', 'push_ipdatetime': '27.52.204.249 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'kingkey88', 'push_content': '還不燒 
她一波！', 'push_ipdatetime': '114.47.38.20 02/10 16:53'}, {'push_tag': '推', 
'push_userid': 'ilovezelda', 'push_content': '槍決', 'push_ipdatetime': '223.138.219.101 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'qwe60038', 'push_content': '一巴掌給他下去', 'push_ipdatetime': '220.134.246.59 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'shevchen', 'push_content': '從前有個好萊塢', 
'push_ipdatetime': '111.253.222.215 02/10 16:53'}, {'push_tag': '噓', 'push_userid': 'chuyuanchan', 'push_content': '拿火槍噴火啊', 'push_ipdatetime': '39.11.6.63 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'elec1141', 'push_content': '燒毀', 'push_ipdatetime': '114.136.166.240 02/10 16:53'}, {'push_tag': '噓', 'push_userid': 'jakewu1217', 'push_content': '燒她', 'push_ipdatetime': '111.250.184.32 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'kawazakiz2', 
'push_content': '你朋友被捅刀，但他沒事的', 'push_ipdatetime': '210.242.52.20 
02/10 16:55'}, {'push_tag': '推', 'push_userid': 'oo2751394', 'push_content': 
'這邊超好笑 但現實悲劇', 'push_ipdatetime': '27.247.38.15 02/10 16:58'}], 'comment_stats': {'all': 14, 'count': -1, 'push': 4, 'boo': 5, 'neutral': 5}}     
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324701.A.27D.html>
{'id': 'M.1581324701.A.27D', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324701.A.27D.html', 'author': 'ben780413 (V6王)', 'title': 'Re: [問卦] 有哪些Youtuber你不退訂卻又不太看的?', 'date': 'Mon Feb 10 16:51:35 2020', 'content': ' 
真心覺得會去迷浩浩、菜啊嘠、寡急、管掌、ㄧ日系列的人到底有多蠢啊\n\n花自己人生
的時間去幫別人充點閱率、幫人家賺錢，然後再靠北政府不拼經濟\n\n與其看迷他們不如
思考國家發展跟環境來得有用\n\n他們的影片不就是炒點話題梗、好笑但也不致於去迷啊
，請問看了那麽多的影片得到什麼\n？\n\n最蠢就是那種影片明白跟你講我要葉配囉然後
還跟著去看去買\n\n人家數錢數的笑呵呵，腦粉還能幫忙護航，愚民時代\n\n V6 25周年
 第51張單曲ある日願いが叶ったんだ/All For You熱賣中 V6 are 20th Century   (美 
聲昌 溫柔博 搞笑井) Coming Century (冷酷剛 可愛健 帥氣准) https://www.ptt.cc/bbs/Gossiping/M.1581324701.A.27D.html', 'comments': [{'push_tag': '推', 'push_userid': 'andy199113', 'push_content': '曾feat政治人物的基本上都不值得一看', 'push_ipdatetime': '220.133.45.155 02/10 16:52'}, {'push_tag': '→', 'push_userid': 'andy199113', 'push_content': '經常接業配廣告的也不值得一看', 'push_ipdatetime': '220.133.45.155 02/10 16:52'}, {'push_tag': '推', 'push_userid': 'aidaP', 'push_content': '五樓只看玉火聖尊', 'push_ipdatetime': '101.15.147.246 02/10 16:53'}, {'push_tag': '推', 'push_userid': 'lovehank1210', 'push_content': ' 
為什麼這麼火大？', 'push_ipdatetime': '111.82.187.186 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'mij', 'push_content': '不能說網紅壞話你會被清高腦粉罵
', 'push_ipdatetime': '111.240.116.39 02/10 16:53'}, {'push_tag': '推', 'push_userid': 'kappaisshit', 'push_content': '對啊那些素質真的低，我都只看艾莉莎', 
'push_ipdatetime': '39.11.37.35 02/10 16:54'}, {'push_tag': '噓', 'push_userid': 'kent00216', 'push_content': '媽的！我打工要死要活，賺的也是老闆啊', 'push_ipdatetime': '101.137.205.83 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'kappaisshit', 'push_content': '莎', 'push_ipdatetime': '39.11.37.35 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'kent00216', 'push_content': '！', 'push_ipdatetime': '101.137.205.83 02/10 16:54'}, {'push_tag': '→', 'push_userid': 
'qwe60038', 'push_content': '阿你就退訂 別看就好', 'push_ipdatetime': '220.134.246.59 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'SkyPlus', 'push_content': '預覽圖有自己大頭的不看，另外不提供文字', 'push_ipdatetime': '140.113.235.116 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'SkyPlus', 'push_content': '搞也不看，我是來學新東西，不是看你的臉', 'push_ipdatetime': '140.113.235.116 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'allanbrook', 'push_content': '很氣喔', 'push_ipdatetime': '61.60.127.23 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'luuuking', 'push_content': 'https://i.imgur.com/ddylXxQ.png', 'push_ipdatetime': '49.216.51.132 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'luuuking', 'push_content': '我還在想誰會去回1/30的文，兄弟，別那', 'push_ipdatetime': '49.216.51.132 02/10 16:56'}, {'push_tag': '→', 'push_userid': 
'luuuking', 'push_content': '麼氣吧...', 'push_ipdatetime': '49.216.51.132 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'superhome', 'push_content': '這 
比喻就跟打電動是浪費時間有87%像', 'push_ipdatetime': '61.219.106.193 02/10 16:57'}, {'push_tag': '噓', 'push_userid': 'yipogo', 'push_content': '明明自己也 
愛看在那邊惱羞什麼呢？', 'push_ipdatetime': '223.136.198.97 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'gg8n8nd34ss', 'push_content': '你自己感覺看超多
 這麼了解XDDDDDDDD', 'push_ipdatetime': '36.228.150.190 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'FUBAR', 'push_content': '確實 腦粉最喜歡在廢片底下
留言刷忠誠度www', 'push_ipdatetime': '123.192.153.194 02/10 16:58'}, {'push_tag': '噓', 'push_userid': 'lsps40803', 'push_content': '何不說說你做了什麼', 'push_ipdatetime': '122.147.234.66 02/10 16:59'}], 'comment_stats': {'all': 21, 
'count': 4, 'push': 7, 'boo': 3, 'neutral': 11}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324711.A.FFD.html>
{'id': 'M.1581324711.A.FFD', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324711.A.FFD.html', 'author': 'linx210145 (hotnet)', 'title': 'Re: [問卦] 把公主
號上面的台灣人接回台灣 你支持嗎', 'date': 'Mon Feb 10 16:51:49 2020', 'content': '別忘了 釣魚島被日本幹走歷史\n\n\n每開過釣魚島 日本地雷達就鎖定\n\n怎可能讓
你輕鬆過去接人\n\n我覺得 20多人就交給日方處理\n\n反正上船都有附贈旅遊保險\n\n 
萬一真的需要醫療 也不用花到錢\n\n建議在日本接受高端醫療（日本醫療技術基本上還 
是比台灣的強）\n\n回來誰也不敢保證沒有風險\n\n相忍為國 : 公主號上面還有20多位 
台灣人，不確定有沒有被感染， : 但如果政府派船把他們接回來台灣，你支持嗎？ https://www.ptt.cc/bbs/Gossiping/M.1581324711.A.FFD.html', 'comments': [{'push_tag': '推', 'push_userid': 'abramtw', 'push_content': '不接回來隔離 等20人一被放 
馬上買機票回', 'push_ipdatetime': '1.200.204.214 02/10 16:53'}, {'push_tag': '推', 'push_userid': 'luuuking', 'push_content': '台灣這次是投下最高資源救你， 
至於日本', 'push_ipdatetime': '49.216.51.132 02/10 16:53'}, {'push_tag': '→', 
'push_userid': 'luuuking', 'push_content': '那個效率，我不覺得醫療會比台灣好....', 'push_ipdatetime': '49.216.51.132 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'abramtw', 'push_content': '台北高雄跑全台', 'push_ipdatetime': '1.200.204.214 02/10 16:53'}, {'push_tag': '推', 'push_userid': 'ilovemygf', 'push_content': '接回來放你家隔離', 'push_ipdatetime': '39.9.71.220 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'abramtw', 'push_content': '如果同意讓他們跑全
台的話 可以不要接', 'push_ipdatetime': '1.200.204.214 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'abramtw', 'push_content': 'Your call!', 'push_ipdatetime': '1.200.204.214 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'netio', 'push_content': '日本要處理3000多人 台灣肯定排後面', 'push_ipdatetime': '175.181.98.4 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'myabcd', 'push_content': '日本案例大多數境外加上那艘船，算有守住', 'push_ipdatetime': '114.32.69.44 02/10 16:59'}], 'comment_stats': {'all': 9, 'count': 4, 'push': 4, 'boo': 0, 'neutral': 5}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324709.A.744.html>
{'id': 'M.1581324709.A.744', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324709.A.744.html', 'author': 'EBVirus (洨洨積極哥)', 'title': '[問卦] 有封城的 
八卦嗎?', 'date': 'Mon Feb 10 16:51:47 2020', 'content': '明明就是封閉式管理\n就是各出入口加強對外交通管制\n然後出入登記量體溫而已\n是豐臣秀吉還是風塵僕僕\n為什麼硬要說人家封城\n有封城的八卦嗎\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324709.A.744.html', 'comments': [{'push_tag': '噓', 'push_userid': 'vbox', 'push_content': '你標題會氣死五毛 = =', 'push_ipdatetime': '1.167.136.108 02/10 16:52'}, {'push_tag': '→', 'push_userid': 'RRADA', 'push_content': '維尼封了 
國境', 'push_ipdatetime': '111.250.145.177 02/10 16:52'}, {'push_tag': '推', 'push_userid': 'GY426', 'push_content': '菸粉不意外 隨便弄就高潮', 'push_ipdatetime': '42.73.248.242 02/10 16:52'}, {'push_tag': '噓', 'push_userid': 'shevchen', 'push_content': '五樓肛門用塞子封住ㄖ', 'push_ipdatetime': '111.253.222.215 02/10 16:52'}, {'push_tag': '推', 'push_userid': 'dai26', 'push_content': '故意的啊', 'push_ipdatetime': '42.77.178.21 02/10 16:53'}, {'push_tag': '推', 
'push_userid': 'wolve', 'push_content': '豐臣公主', 'push_ipdatetime': '49.215.137.90 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'yafx4200p', 'push_content': 'https://www.douyu.com/5987284  廣州塔', 'push_ipdatetime': '220.133.115.236 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'yafx4200p', 'push_content': '直播 看起來還可以', 'push_ipdatetime': '220.133.115.236 02/10 16:59'}], 'comment_stats': {'all': 8, 'count': 2, 'push': 4, 'boo': 2, 'neutral': 2}}  
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324929.A.791.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581325192.A.9B5.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324975.A.75D.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324891.A.EA8.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324943.A.DFB.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324779.A.856.html>
{'id': 'M.1581324779.A.856', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324779.A.856.html', 'author': 'g8956956 (低調的手滑)', 'title': '[問卦]疫情嚴重 
去對岸工作的怎麼辦？', 'date': 'Mon Feb 10 16:52:57 2020', 'content': '小弟剛 
好有親戚在對岸經商、工作\n\n現在越看各種新聞真的越抖。\n\n像現在中國各地各省，
幾乎都要分小區隔離，\n\n大公司如台積南京廠那些台幹怎麼辦？\n\n台積電真的沒打算
預先準備？\n\n（自己投資當老闆的就算了，台幹只是吃人薪\n\n水，辭職就只能喝西北
風了）\n\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324779.A.856.html', 'comments': [{'push_tag': '推', 'push_userid': 's820912gmail', 'push_content': 'rip', 'push_ipdatetime': '115.82.180.171 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'zxc2331189', 'push_content': '不爽去還有其他人等著去啊', 'push_ipdatetime': '115.82.163.130 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'powyo', 'push_content': '另謀高就', 'push_ipdatetime': '118.163.229.98 02/10 16:53'}, {'push_tag': '→', 'push_userid': 'reachhard', 'push_content': '我家人就台幹  
公司直接叫他們不要去', 'push_ipdatetime': '58.115.188.6 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'reachhard', 'push_content': '在家辦公', 'push_ipdatetime': '58.115.188.6 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'jmss50894', 'push_content': 'https://imgur.com/MoHs5Hg.jpg', 'push_ipdatetime': '61.228.14.116 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'Arad', 'push_content': '自己衡量辣 中鏢 公司要不要負責', 'push_ipdatetime': '180.217.195.248 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'aidaP', 'push_content': '改去別
國工作', 'push_ipdatetime': '101.15.147.246 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'snow3804', 'push_content': '台幹:我只是吃人薪水,台灣快派專機救 
我', 'push_ipdatetime': '114.44.145.86 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'gunfighter', 'push_content': '去阿 去了就不用回來了 不然還怎麼辦', 
'push_ipdatetime': '27.242.69.78 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'snow3804', 'push_content': '我跟台商不一樣,台商可以不救,但要救我', 'push_ipdatetime': '114.44.145.86 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'hitomitw', 'push_content': '我朋友是台幹，他們公司台幹聯合向公司', 'push_ipdatetime': '140.136.182.5 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'hitomitw', 'push_content': '請願延後開工，公司有同意', 'push_ipdatetime': '140.136.182.5 02/10 16:59'}], 'comment_stats': {'all': 13, 'count': 4, 'push': 4, 'boo': 
0, 'neutral': 9}}
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324967.A.037.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324879.A.3F7.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581325139.A.85F.html>
{'id': 'M.1581325139.A.85F', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581325139.A.85F.html', 'author': 'seth5421 (正版廢文王)', 'title': '[問卦] 聽過最中
二的一句話', 'date': 'Mon Feb 10 16:58:57 2020', 'content': '嗨嗨我是廢廢\n廢 
廢最近喜歡上\n看看國中屁孩語錄\n像是一張玉米鬚頭的照片\n配上我看不到未來\n這句
\n覺得很中二\n但有沒有其他更中二的台詞呢\n有沒有八卦\n嘻嘻\n\n\nSent from JPTT on my Samsung SMG935F.\n\n https://www.ptt.cc/bbs/Gossiping/M.1581325139.A.85F.html', 'comments': [{'push_tag': '推', 'push_userid': 'kcclasaki', 'push_content': '二樓金城武', 'push_ipdatetime': '118.171.235.101 02/10 16:59'}, {'push_tag': '推', 'push_userid': 'wwimd135697', 'push_content': '噁男', 'push_ipdatetime': '36.236.31.157 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'GY426', 'push_content': '樓下被肛的時候會怎麼叫??', 'push_ipdatetime': '42.73.248.242 02/10 16:59'}, {'push_tag': '推', 'push_userid': 's820912gmail', 'push_content': '我帥！', 'push_ipdatetime': '115.82.180.171 02/10 16:59'}], 'comment_stats': {'all': 4, 'count': 3, 'push': 3, 'boo': 0, 'neutral': 1}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581325177.A.1D9.html>
{'id': 'M.1581325177.A.1D9', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581325177.A.1D9.html', 'author': 'vbox (小孩)', 'title': 'Re: [問卦] 之前看到chinese taipei就抓狂的人 痊癒沒', 'date': 'Mon Feb 10 16:59:35 2020', 'content': ': 
 引述《syearth (sysearth)》之銘言： : : 請問一下 : : [新聞] 台灣：將以Chinese 
Taipei出席WHO : : 加上今年東京奧運 也是要用chinese taipei參賽 : : 之前看到chinese taipei就抓狂的人 痊癒了嗎? : 政治就是這樣玩的 : 別人不可以，我可以 : 總統 
兼任黨主席、黨意立委、砍七天假 : 一大堆說不完 跪來的中共很爽的 > 人民罵\n\n爭 
來的中共很不爽的 > 人民開心\n\n https://www.ptt.cc/bbs/Gossiping/M.1581325177.A.1D9.html', 'comments': [], 'comment_stats': {'all': 0, 'count': 0, 'push': 0, 'boo': 0, 'neutral': 0}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581325010.A.AD0.html>
{'id': 'M.1581325010.A.AD0', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581325010.A.AD0.html', 'author': 'widec (☑30cm)', 'title': '[問卦] 是不是應該宣導全
戴口罩比較好', 'date': 'Mon Feb 10 16:56:48 2020', 'content': '借用中研院何美 
鄉這支影片 https://youtu.be/In_nouiwv8?t=370 投影簡報裡的圖 https://imgur.com/HjrUHtl 何美鄉圖示了飛沫如何傳播的曲線途徑\n說明了勤洗手比戴口罩重要\n因為你不
見得會被咳嗽噴到\n手卻一定會無意識亂摸\n\n那如果宣導全國人民都戴口罩 只不過戴 
的是可換洗的布口罩 外科口罩留待大爆發時才戴\n\n噴的一方飛沫噴在布口罩上已經攔 
掉一部份\n被噴的一方至少有布口罩再攔掉一部份\n再配合所有公共場所廣置乾洗手\n\n是不是會比宣導大眾運輸工具是開放空間\n更有腦、而且有效？\n\n https://www.ptt.cc/bbs/Gossiping/M.1581325010.A.AD0.html', 'comments': [{'push_tag': '→', 'push_userid': 'kawazakiz2', 'push_content': '買不到是要怎麼戴你戴給我看啊', 'push_ipdatetime': '210.242.52.20 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'testutw', 'push_content': '韓導粉不要再發表反政府言論 滾', 'push_ipdatetime': '211.20.23.127 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'Horatio5566', 'push_content': '怎麼不宣導 不要坐捷運??', 'push_ipdatetime': '115.43.230.213 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'bearq258', 'push_content': '去
買幾個防護頭套卡安全', 'push_ipdatetime': '122.121.120.36 02/10 16:59'}, {'push_tag': '推', 'push_userid': 'kiddcat', 'push_content': '有病就趕快去看醫師,不
要自己買藥吃', 'push_ipdatetime': '1.163.30.54 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'PompelmousJ', 'push_content': '你先把多的口罩寄給我', 'push_ipdatetime': '111.71.40.0 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'ayakiax', 'push_content': '請不要質疑黨', 'push_ipdatetime': '223.138.99.188 02/10 16:59'}], 'comment_stats': {'all': 7, 'count': 1, 'push': 1, 'boo': 0, 'neutral': 6}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324991.A.CB4.html>
{'id': 'M.1581324991.A.CB4', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324991.A.CB4.html', 'author': 'deltaz (我還懂不懂飛翔)', 'title': 'Re: [問卦] 一
芳新聞天天爆  皮件公司沒新聞', 'date': 'Mon Feb 10 16:56:29 2020', 'content': 
'吹哨人是打政府的1922專線投訴，結果資料外洩被革職，這條超大欸\n\n八卦版怎麼能 
容許有政府官員瀆職成這樣還不開罵啊? 啊，是DPP，沒事沒事\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324991.A.CB4.html', 'comments': [{'push_tag': '→', 'push_userid': 'iPadProPlus', 'push_content': '正解', 'push_ipdatetime': '101.12.42.223 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'alex00089', 'push_content': '公關很厲害', 'push_ipdatetime': '220.138.106.191 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'deann', 'push_content': '1922專線誰管的 就是誰外洩檢 
舉人資料阿', 'push_ipdatetime': '61.220.51.98 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': '中華電信表示:', 'push_ipdatetime': '39.12.32.241 02/10 16:59'}], 'comment_stats': {'all': 4, 'count': 1, 'push': 1, 'boo': 0, 'neutral': 3}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581325012.A.8EA.html>
{'id': 'M.1581325012.A.8EA', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581325012.A.8EA.html', 'author': 'MagicYif (魔法義夫)', 'title': '[問卦] 現在印度是
不是人類最後生存指標', 'date': 'Mon Feb 10 16:56:50 2020', 'content': '印度人 
生活在上游燒屍體下游接起來喝的恆河\n排隊都是懶叫貼屁股的距離\n路邊小販攤子上的
食物經過一整天的廢氣 灰塵 口水\n照樣徒手抓起來賣給你\n如此艱困的環境養成了印度
人百毒不侵的體質 到現在還沒有確診\n\n所以如果連印度都淪陷了\n是不是代表人類就 
快掛了?\n\n\n\n https://www.ptt.cc/bbs/Gossiping/M.1581325012.A.8EA.html', 'comments': [{'push_tag': '推', 'push_userid': 'pdz', 'push_content': '乾淨又衛生
', 'push_ipdatetime': '211.72.53.136 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'davideason', 'push_content': '恆河或成最大贏家', 'push_ipdatetime': '42.77.34.27 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'lovehank1210', 'push_content': '印度 唯一淨土', 'push_ipdatetime': '111.82.187.186 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'w9103', 'push_content': '達爾文的天擇', 'push_ipdatetime': '111.248.160.68 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'k960674', 'push_content': '印度路邊小吃真的超毒', 'push_ipdatetime': '42.73.17.127 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'akway', 'push_content': '20年後 地球只剩印度人', 'push_ipdatetime': '114.44.109.26 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'vinca', 'push_content': '會進化成新人類
', 'push_ipdatetime': '1.200.204.174 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'moebius2', 'push_content': '印度人:多喝恆河水 保證不怕肺炎', 'push_ipdatetime': '110.90.114.177 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'aidaP', 'push_content': '以毒攻毒啊', 'push_ipdatetime': '101.15.147.246 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'heyd', 'push_content': '難怪未來人 
說印度會征服世界', 'push_ipdatetime': '114.41.71.83 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'Horatio5566', 'push_content': '病毒在恆河都活不下去 缺 
氧毒死', 'push_ipdatetime': '115.43.230.213 02/10 16:58'}, {'push_tag': '推', 
'push_userid': 'bill403777', 'push_content': '沒確診是因為根本沒在驗吧', 'push_ipdatetime': '123.51.142.8 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'sulaman', 'push_content': '受加持的恆河水', 'push_ipdatetime': '223.141.92.92 
02/10 16:58'}, {'push_tag': '推', 'push_userid': 'DustToDust', 'push_content': '阿三連核戰都撐過來了', 'push_ipdatetime': '36.232.249.126 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'krthree', 'push_content': '印度煉蠱上千年，果 
然是神選之民', 'push_ipdatetime': '1.161.48.251 02/10 16:58'}, {'push_tag': ' 
推', 'push_userid': 'PompelmousJ', 'push_content': '印度或成最大贏家', 'push_ipdatetime': '111.71.40.0 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'ziso', 'push_content': '肚子裝恆河水 百毒不侵', 'push_ipdatetime': '211.72.185.125 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'GY426', 'push_content': '印
度gpx', 'push_ipdatetime': '42.73.248.242 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'bread220', 'push_content': '孟加拉應該也可以', 'push_ipdatetime': '59.125.187.85 02/10 16:59'}, {'push_tag': '推', 'push_userid': 'luuuking', 'push_content': '10億種DNA的試煉', 'push_ipdatetime': '49.216.51.132 02/10 16:59'}, {'push_tag': '推', 'push_userid': 'abramtw', 'push_content': '他們連3020 
冠狀病毒的抗體都有了', 'push_ipdatetime': '1.200.204.214 02/10 16:59'}], 'comment_stats': {'all': 21, 'count': 16, 'push': 16, 'boo': 0, 'neutral': 5}}     
2020-02-10 17:00:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1581324860.A.7A1.html> (referer: https://www.ptt.cc/bbs/Gossiping/index.html)
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324929.A.791.html>
{'id': 'M.1581324929.A.791', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324929.A.791.html', 'author': 'lw5575 ()', 'title': '[問卦] 皰疹病毒，不會消失的
八卦？', 'date': 'Mon Feb 10 16:55:27 2020', 'content': '聽說有一種皰疹病毒\n\n大多數人會長在嘴唇\n\n偶爾長出\n\n擦藥之後~表面好了\n\n但聽說病毒還是躲在深處
\n\n\n\n為什麼會這樣？\n\n藥殺不到嗎\n\n\n\n研發奈米機器人抓病毒有可能嗎?\n\n\n\n\n\n專家來分析分析\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324929.A.791.html', 'comments': [{'push_tag': '→', 'push_userid': 'omfg5487', 'push_content': '蓋', 'push_ipdatetime': '1.200.210.117 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'zxc2331189', 'push_content': '五樓龜頭上漲很多 問她', 'push_ipdatetime': '115.82.163.130 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'omfg5487', 'push_content': '旋風 
蓋', 'push_ipdatetime': '1.200.210.117 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'zxc2331189', 'push_content': '超陷害蓋', 'push_ipdatetime': '115.82.163.130 02/10 16:56'}, {'push_tag': '噓', 'push_userid': 'luke11130177', 'push_content': '五樓長在那裡', 'push_ipdatetime': '61.228.247.23 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'powyo', 'push_content': '5樓很有經驗', 'push_ipdatetime': '118.163.229.98 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': '就跟細胞共存 ... 抵抗力一差 就作亂', 'push_ipdatetime': '39.12.32.241 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'luke11130177', 'push_content': '我一定吉', 'push_ipdatetime': '61.228.247.23 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'viable', 'push_content': 'yeah~trouble shingle viruses', 'push_ipdatetime': '101.136.46.21 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'iPadProPlus', 'push_content': '就潛伏著，沒事做', 'push_ipdatetime': '101.12.42.223 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'jimmykuo123', 'push_content': '把神經切光就可以根治了吧XDD', 'push_ipdatetime': '111.251.43.248 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'kawazakiz2', 'push_content': '五樓長在哪快說', 'push_ipdatetime': '210.242.52.20 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'Gsanz', 'push_content': '病毒躲在神經
節裡面', 'push_ipdatetime': '59.126.186.120 02/10 16:58'}, {'push_tag': '推', 
'push_userid': 'EggAcme', 'push_content': '病毒類大多不好搞阿', 'push_ipdatetime': '36.234.145.118 02/10 16:59'}, {'push_tag': '推', 'push_userid': 'viable', 'push_content': 'it attack nerve cells when people get', 'push_ipdatetime': 
'101.136.46.21 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'viable', 'push_content': 'weak, but not necessary have any bre', 'push_ipdatetime': '101.136.46.21 02/10 16:59'}], 'comment_stats': {'all': 16, 'count': 4, 'push': 5, 'boo': 1, 'neutral': 10}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...        
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581325192.A.9B5.html>
{'id': 'M.1581325192.A.9B5', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581325192.A.9B5.html', 'author': 'ffreakk ()', 'title': 'Re: [問卦] 為什麼台灣拍不 
出寄生上流？', 'date': 'Mon Feb 10 16:59:48 2020', 'content': ': 剛得知寄生上 
流獲選奧斯卡最佳影片 : 相較之下台灣真可悲，別說得獎 : 10幾年來連提名都沒機會 : 一堆人還在返校神作，洋洋得意 : 你眼中的神作在別人看來什麼都不是 : 台灣人什麼 
不會最會的就是無限膨脹自己 : 這幾天就好幾篇自吹自擂的文章在洗文 : 韓國也沒比台
灣大多少 : 人口也沒多台灣好幾倍 : 台灣前幾年還看不起人家 : 結果人均慘輸、運動 
慘輸、科技樹慘輸 : 韓國一個小國家出了現代起亞，全球五大車廠 : 台灣有什麼？ :  
還在最美麗的風景喔？ : 什麼時候才會正視自己的缺點努力追上韓國？ 台灣有蔡明亮  
侯孝賢 李安 齊柏林\n\n算很厲害了\n\n當年臥虎藏龍得奬\n\n墊在奧斯卡小金人下面的
\n\n就是幾十年的武俠小說跟電影\n\n那是文化累積財\n\n\n寄生上流台灣當然拍不出來
\n\n能拍出來的\n\n是親身見證香港住劏房的香港人\n\n因為台灣的財團家族沒那麼惹人
厭\n\n底下階層\n\n日子也不夠苦\n\n台灣窮人相對是比較容易向上流動的\n\n起碼有健
保 家庭經濟不會輕易被拖垮\n\n\n每個社會有自己的社會問題\n\n能有資金願意投入拍 
這種批判性質的電影\n\n韓國一方面是影視產業欣欣向榮\n\n另一方面 是一種社會責任 
感\n\n台灣沒有這種電影\n\n是相對之下政通人和 兩性平等\n\n導演跟編劇取材\n\n就 
會轉彎到社會中人的問題\n\n二代之間的衝突等等\n\n韓國也拍不出喜宴好嗎\n\n同志議
題還在櫃子裡\n\n\n\n https://www.ptt.cc/bbs/Gossiping/M.1581325192.A.9B5.html', 'comments': [], 'comment_stats': {'all': 0, 'count': 0, 'push': 0, 'boo': 0, 'neutral': 0}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324975.A.75D.html>
{'id': 'M.1581324975.A.75D', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324975.A.75D.html', 'author': 'ElectronPair (電子隊)', 'title': '[問卦] 屍速列車
是怎麼把疫情控制住的', 'date': 'Mon Feb 10 16:56:13 2020', 'content': '從一開 
始的生化感染了一頭鹿\n到之後人咬人\n咬到之後沒幾分鐘就感染\n這期間一定更多災情
吧\n怎麼可能一個釜山控制了就沒事了\n劇情也沒發明特效藥，只是武力鎮壓\n其他地方
，其他國家都沒疫情不是很奇怪嗎？\n有沒有真實世界這種劇情還能可控可防的機率有多
大的八卦\n光看武漢肺炎蔓延全世界就知道了\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324975.A.75D.html', 'comments': [{'push_tag': '噓', 'push_userid': 'Sougetu', 'push_content': '你們是講好的嗎', 'push_ipdatetime': '36.226.95.66 02/10 16:56'}, {'push_tag': '噓', 'push_userid': 'yeng1217', 'push_content': '沒演 
啊', 'push_ipdatetime': '114.137.39.220 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'AOA2', 'push_content': '劇中並沒有演到其他地方沒疫情吧~只是沒提到', 'push_ipdatetime': '117.56.61.24 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'MVPGGYY', 'push_content': '就封住進斧山的路啊', 'push_ipdatetime': '180.217.117.234 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'tw15', 'push_content': '就沒控制住 但是要拍片得獎 其他人通通死光', 'push_ipdatetime': '219.71.91.194 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'chow365', 'push_content': '殺光', 'push_ipdatetime': '101.12.61.241 02/10 16:57'}, {'push_tag': '推
', 'push_userid': 'KEYork', 'push_content': '殭屍不會做飛機，不會開門。', 'push_ipdatetime': '27.52.131.94 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'clst', 'push_content': '這種有得病傳染力的一看就知道還比較簡單', 'push_ipdatetime': '210.66.181.112 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'Lindseyy', 'push_content': '孔劉就是帥阿', 'push_ipdatetime': '180.217.82.62 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'netio', 'push_content': '又沒演完~', 'push_ipdatetime': '175.181.98.4 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'ericeuro', 'push_content': '感染速度太快，根本不會傳到其他國家', 'push_ipdatetime': '42.72.100.23 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'snow3804', 'push_content': '第二集劇本還在看中國是怎麼演的', 'push_ipdatetime': '114.44.145.86 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'Jess12', 'push_content': '沒控制住吧！', 'push_ipdatetime': '42.72.242.250 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'clst', 'push_content': '現在這種中了還不知道誰
傳給你的更困難', 'push_ipdatetime': '210.66.181.112 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'clst', 'push_content': '而且屍速列車的感染者可以撲殺 簡
單多了', 'push_ipdatetime': '210.66.181.112 02/10 16:59'}], 'comment_stats': {'all': 15, 'count': 5, 'push': 7, 'boo': 2, 'neutral': 6}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324891.A.EA8.html>
{'id': 'M.1581324891.A.EA8', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324891.A.EA8.html', 'author': 'Chenwei35 (Wei)', 'title': '[問卦] 潛伏期傳染', 'date': 'Mon Feb 10 16:54:49 2020', 'content': '因公司業務頻繁的與陸港相關人員 
有機會接觸到 (當然基本會戴口罩)\n剛在會議結束前  meeting host 以大家要看顧好身
體健康做結尾\n(心裡不免OS說那還一直找大家開會真心建議公司這個節骨眼都採電話或 
視訊會議)\n\n回到問題是:\n假如A君今天被感染但處於潛伏期B君不慎被潛伏期的A君感 
染到\n但A君本身免疫力極佳在輕微症狀之下就自體恢復健康\n而衰小的B君體弱被A君感 
染後症狀嚴重被隔離\n但這之間B根本不知道原來帶原者是A君以致這之間A君跟本不知道 
自己是帶原者\n傳染了給C D E ...\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324891.A.EA8.html', 'comments': [{'push_tag': '推', 'push_userid': 'omfg5487', 'push_content': '蓋', 'push_ipdatetime': '1.200.210.117 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'iPadProPlus', 'push_content': '早就知道了吧', 'push_ipdatetime': '101.12.42.223 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'victoryss', 'push_content': '恩然後?', 'push_ipdatetime': '111.254.20.125 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'jmss50894', 'push_content': '陸甚 
麼陸 企鵝逆', 'push_ipdatetime': '61.228.14.116 02/10 16:55'}, {'push_tag': ' 
推', 'push_userid': 'firelin', 'push_content': '反正會沒完沒了，只能發展疫苗了
', 'push_ipdatetime': '180.204.64.108 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'NaoGaTsu', 'push_content': '是有可能啊 但會問你接觸史啊', 'push_ipdatetime': '61.230.11.202 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'liusim', 'push_content': '多洗手 不要亂摸鼻子眼睛嘴巴 別胡思亂想', 'push_ipdatetime': '114.41.58.112 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'wtowillie', 'push_content': '目前只能等疫苗，不然無解', 'push_ipdatetime': '27.242.100.29 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'firelin', 'push_content': '每個人衛生習慣好，傳染就慢', 'push_ipdatetime': '180.204.64.108 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'firelin', 'push_content': '這可能會是新流感
，所以只能共存來對付', 'push_ipdatetime': '180.204.64.108 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'closedltw', 'push_content': '問接觸史也沒用,無法 
證明B是被A傳染的', 'push_ipdatetime': '219.87.85.162 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'firelin', 'push_content': '越來越多專家會發表這樣看法 
的...', 'push_ipdatetime': '180.204.64.108 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'firelin', 'push_content': 'sars幾乎重症，所以無共存問題', 'push_ipdatetime': '180.204.64.108 02/10 16:58'}, {'push_tag': '推', 'push_userid': 
'OgOl', 'push_content': '感覺跟B肝一樣了', 'push_ipdatetime': '223.141.206.194 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'firelin', 'push_content': ' 
流感輕症多，少數重症。無法消滅', 'push_ipdatetime': '180.204.64.108 02/10 16:59'}], 'comment_stats': {'all': 15, 'count': 6, 'push': 6, 'boo': 0, 'neutral': 9}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324943.A.DFB.html>
{'id': 'M.1581324943.A.DFB', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324943.A.DFB.html', 'author': 'smd1201 ()', 'title': 'Re: [爆卦] 80台藝人集體錄 
影為武漢肺炎祈禱發聲', 'date': 'Mon Feb 10 16:55:41 2020', 'content': '中國最 
近派軍機繞台灣 台灣藝人沉默不語\n\n    中國阻止台灣加入WHO 台灣藝人沉默不語\n\n    中國一天到晚嗆要武統台灣 台灣藝人沉默不語\n\n    武漢肺炎在中國蔓延 台灣 
藝人就齊祈禱發聲\n\n    難道武漢肺炎在台灣都沒病例嗎？\n\n    難道台灣人的生命
安全比不上中國人的生命安全嗎？\n\n    這些藝人竟然敢說自己是台灣藝人\n\n    真
的很看不起這些人\n\n    噁心的一群人\n\n    難怪台灣的演藝產業輸韓國那麼多\n\n\n\n\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324943.A.DFB.html', 'comments': [{'push_tag': '推', 'push_userid': 'louis5265', 'push_content': '支那是源頭 
，藝人不講話', 'push_ipdatetime': '49.214.226.157 02/10 16:57'}, {'push_tag': 
'→', 'push_userid': 'jetaime851', 'push_content': '是比不上啊 你肥宅能怎樣 萬 
用抵制？', 'push_ipdatetime': '111.82.167.226 02/10 16:58'}, {'push_tag': '推', 'push_userid': 'wds824', 'push_content': '別這樣，一堆粉絲會玻璃的', 'push_ipdatetime': '180.217.134.253 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'hihimen', 'push_content': '在公海上繞台灣，你緊張什麼?', 'push_ipdatetime': '1.34.233.65 02/10 16:59'}], 'comment_stats': {'all': 4, 'count': 2, 'push': 2, 
'boo': 0, 'neutral': 2}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324967.A.037.html>
{'id': 'M.1581324967.A.037', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324967.A.037.html', 'author': 'DDRMIX (約翰．史密斯)', 'title': '[問卦] 屍速列車
2會找成龍來拍嗎', 'date': 'Mon Feb 10 16:56:05 2020', 'content': '聽說屍速列車
要拍第2集了\n想說最近武漢肺炎這麼嚴重\n如果第2集的背景設定在中國\n並找武打明星
成龍來主演\n不知道會不會更有看頭呢\n\n有沒有屍速列車2的八卦？\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324967.A.037.html', 'comments': [{'push_tag': '→', 
'push_userid': 'kawazakiz2', 'push_content': '火車上要怎麼塞鐵梯', 'push_ipdatetime': '210.242.52.20 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'powyo', 'push_content': '應該是甄子丹', 'push_ipdatetime': '118.163.229.98 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'Lindseyy', 'push_content': '決戰武漢', 'push_ipdatetime': '180.217.82.62 02/10 16:56'}, {'push_tag': '推', 'push_userid': 'juicylove', 'push_content': '會從車廂打到車頂', 'push_ipdatetime': '223.140.19.117 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'io45for222', 'push_content': '結尾 成龍:不怕 中国的病毒會爆炸', 'push_ipdatetime': '211.22.222.46 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'kaiiibao', 'push_content': '喪屍的頭太硬 打完痛的甩手', 'push_ipdatetime': '111.82.140.237 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'jass87987', 'push_content': '景甜演女研
究人員但沒人記得她', 'push_ipdatetime': '36.236.77.32 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'Kelvinchen', 'push_content': '會用椅子擋住一群活屍，
打活屍打到手', 'push_ipdatetime': '114.41.124.188 02/10 16:57'}, {'push_tag': 
'→', 'push_userid': 'Kelvinchen', 'push_content': '痛在那甩手', 'push_ipdatetime': '114.41.124.188 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'hanoo960071', 'push_content': '男主角 陳港生', 'push_ipdatetime': '223.136.114.252 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'akuma183', 'push_content': '會 
在椅子旁的欄杆跳過來跳過去', 'push_ipdatetime': '122.117.171.223 02/10 16:59'}, {'push_tag': '噓', 'push_userid': 'leeeadsl', 'push_content': '問我國家怎會 
染病', 'push_ipdatetime': '36.229.83.109 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'AOA2', 'push_content': '成龍要跟誰打?如果能夠像馬錫東那樣跟喪屍打', 'push_ipdatetime': '117.56.61.24 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'AOA2', 'push_content': '還算有看頭~套來跳去~甩手~用冰箱門撞喪屍頭', 'push_ipdatetime': '117.56.61.24 02/10 16:59'}], 'comment_stats': {'all': 14, 'count': 5, 'push': 6, 'boo': 1, 'neutral': 7}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324879.A.3F7.html>
{'id': 'M.1581324879.A.3F7', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324879.A.3F7.html', 'author': 'tetani (喵喵)', 'title': 'Re: [問卦] 之前看到chinese taipei就抓狂的人 痊癒沒', 'date': 'Mon Feb 10 16:54:37 2020', 'content': ': 請問一下 : [新聞] 台灣：將以Chinese Taipei出席WHO : 加上今年東京奧運 也是要 
用chinese taipei參賽 : 之前看到chinese taipei就抓狂的人 痊癒了嗎? 政治就是這樣
玩的\n別人不可以，我可以\n總統兼任黨主席、黨意立委、砍七天假\n一大堆說不完\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324879.A.3F7.html', 'comments': [{'push_tag': '→', 'push_userid': 'jmss50894', 'push_content': 'chinks阿哈哈哈', 'push_ipdatetime': '61.228.14.116 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'tml7415', 'push_content': '你能嘴的就這幾項而已啦 國民黨每項都爛', 'push_ipdatetime': '39.12.32.241 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'poggssi', 'push_content': '雙標黨不意外，蟑螂也乖乖吞下去，笑死', 'push_ipdatetime': '111.71.97.103 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'poggssi', 'push_content': '二樓，你確定只有這幾個能嘴？', 'push_ipdatetime': '111.71.97.103 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': 
'每一項國民黨都更爛 你還不選民進黨 傻?', 'push_ipdatetime': '39.12.32.241 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'testutw', 'push_content': '蠢吱被
巴臉到腫的跟麵龜一樣就會拉狗黨', 'push_ipdatetime': '211.20.23.127 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'testutw', 'push_content': '救援 果然是兩
個垃圾濫檔', 'push_ipdatetime': '211.20.23.127 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': '817萬票  哈哈哈哈哈 大勝 懂嗎？', 'push_ipdatetime': '39.12.32.241 02/10 16:57'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': '時代 民眾 連國民黨這種更爛都贏不了', 'push_ipdatetime': '39.12.32.241 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'tml7415', 'push_content': '你就繼續自慰吧', 'push_ipdatetime': '39.12.32.241 02/10 
16:58'}], 'comment_stats': {'all': 10, 'count': 1, 'push': 1, 'boo': 0, 'neutral': 9}}
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: process_item ...
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: process_item ...
2020-02-10 17:00:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1581324860.A.7A1.html>
{'id': 'M.1581324860.A.7A1', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1581324860.A.7A1.html', 'author': 'TomFord5566 (湯福56)', 'title': '[問卦] 台灣醫療 
以餐廳來比喻大概是什麼等級？', 'date': 'Mon Feb 10 16:54:18 2020', 'content': 
'美國醫療雖然一直被靠北很貴\n\n\n但是如果錢催下去\n\n\n那麼就能獲得大概是全世 
界最先進的治療\n\n\n拿餐廳來比大概是米其林三星牛排館之類的\n\n\n好奇世界第一的
台灣醫療如果拿餐廳來比喻\n\n\n大概是哪種比喻才適當？\n\n https://www.ptt.cc/bbs/Gossiping/M.1581324860.A.7A1.html', 'comments': [{'push_tag': '→', 'push_userid': 's820912gmail', 'push_content': '屎尿', 'push_ipdatetime': '115.82.180.171 02/10 16:54'}, {'push_tag': '→', 'push_userid': 'jmss50894', 'push_content': '五星  https://imgur.com/MoHs5Hg.jpg', 'push_ipdatetime': '61.228.14.116 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'GY426', 'push_content': '我家巷
口', 'push_ipdatetime': '42.73.248.242 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'a4162090', 'push_content': '巷口滷肉飯?', 'push_ipdatetime': '61.228.195.172 02/10 16:54'}, {'push_tag': '推', 'push_userid': 'victoryss', 'push_content': '黃金賽亞奈米屌', 'push_ipdatetime': '111.254.20.125 02/10 16:54'}, 
{'push_tag': '推', 'push_userid': 'King5566', 'push_content': '樓下第一次被肛 
是在哪', 'push_ipdatetime': '111.82.83.97 02/10 16:55'}, {'push_tag': '推', 'push_userid': 'gg8n8nd34ss', 'push_content': '299火鍋吃到飽 然後可以另外加點食', 'push_ipdatetime': '36.228.150.190 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'gg8n8nd34ss', 'push_content': '材吧', 'push_ipdatetime': '36.228.150.190 02/10 16:55'}, {'push_tag': '→', 'push_userid': 'iPadProPlus', 'push_content': '我家巷口', 'push_ipdatetime': '101.12.42.223 02/10 16:55'}, {'push_tag': 
'推', 'push_userid': 'Horatio5566', 'push_content': '無國界料理   西醫中醫合併
', 'push_ipdatetime': '115.43.230.213 02/10 16:56'}, {'push_tag': '→', 'push_userid': 'aidaP', 'push_content': '麥當勞', 'push_ipdatetime': '101.15.147.246 
02/10 16:56'}, {'push_tag': '→', 'push_userid': 'glion', 'push_content': '7-11', 'push_ipdatetime': '220.133.77.237 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'coldeden', 'push_content': '便利商店 包山包海大家都負擔得起', 'push_ipdatetime': '218.164.18.23 02/10 16:57'}, {'push_tag': '推', 'push_userid': 'e7660239', 'push_content': '廉價吃到飽', 'push_ipdatetime': '59.127.52.174 02/10 16:57'}, {'push_tag': '噓', 'push_userid': 'Justinniger', 'push_content': '299吃到飽', 'push_ipdatetime': '27.52.0.176 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'alex00089', 'push_content': '比較弱的吃到飽', 'push_ipdatetime': '220.138.106.191 02/10 16:58'}, {'push_tag': '→', 'push_userid': 'skuderic', 'push_content': '吃到飽阿 花沒多少錢 愛怎麼吃怎麼吃 還', 'push_ipdatetime': '101.12.141.124 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'skuderic', 'push_content': '可以哭么菜難吃 廚師沒廚德 收費太貴 等', 'push_ipdatetime': '101.12.141.124 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'skuderic', 'push_content': '到餐廳得獎世界第一 又跳出來沾沾自喜', 'push_ipdatetime': '101.12.141.124 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'skuderic', 'push_content': '倒是沒看到多少人注意後面廚師 服務生辛', 'push_ipdatetime': '101.12.141.124 02/10 16:59'}, {'push_tag': '→', 'push_userid': 'skuderic', 'push_content': '勞的 呵呵', 'push_ipdatetime': '101.12.141.124 02/10 16:59'}], 'comment_stats': {'all': 21, 'count': 7, 'push': 8, 'boo': 1, 'neutral': 12}}
2020-02-10 17:00:01 [scrapy.core.engine] INFO: Closing spider (finished)
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Start: close_spider ...        
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: Save result at E:\Code\dev-projects\Cupoy\pycrawler\myproject\crawled_data\20200210T170000-20200210T170001.json
2020-02-10 17:00:01 [ptt_board_crawler] DEBUG: End: close_spider ...
2020-02-10 17:00:01 [scrapy.statscollectors] INFO: Dumping Scrapy stats:      
{'downloader/request_bytes': 7592,
 'downloader/request_count': 21,
 'downloader/request_method_count/GET': 21,
 'downloader/response_bytes': 63142,
 'downloader/response_count': 21,
 'downloader/response_status_count/200': 20,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 1.500621,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 2, 10, 9, 0, 1, 629469),
 'item_scraped_count': 19,
 'log_count/DEBUG': 103,
 'log_count/INFO': 11,
 'log_count/WARNING': 2,
 'request_depth_max': 1,
 'response_received_count': 21,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 20,
 'scheduler/dequeued/memory': 20,
 'scheduler/enqueued': 20,
 'scheduler/enqueued/memory': 20,
 'start_time': datetime.datetime(2020, 2, 10, 9, 0, 0, 128848)}
2020-02-10 17:00:01 [scrapy.core.engine] INFO: Spider closed (finished)
```
