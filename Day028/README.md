D28：Scrapy 爬蟲流程 (3) - API
=====

Code
-----
[commit](https://github.com/BbsonLin/cupoy-pycrawler-2019/commit/54552ecb6d0f98fb39477c695371424cf68ac0f4#diff-6f0a571d1678836e1bd0c282f5178fb1)

Output
-----

```
PS E:\Code\dev-projects\Cupoy\pycrawler\myproject> python .\main.py -f ptt-gossip.json
2020-01-22 10:41:54 [scrapy.utils.log] INFO: Scrapy 1.8.0 started (bot: myproject)
2020-01-22 10:41:54 [scrapy.utils.log] INFO: Versions: lxml 4.4.2.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 19.10.0, Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Windows-10-10.0.18362-SP0    
2020-01-22 10:41:54 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'myproject', 'NEWSPIDER_MODULE': 'myproject.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['myproject.spiders']}
2020-01-22 10:41:54 [scrapy.extensions.telnet] INFO: Telnet Password: a9bc50aab49e67fe
2020-01-22 10:41:54 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2020-01-22 10:41:54 [scrapy.middleware] INFO: Enabled downloader middlewares:
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
2020-01-22 10:41:54 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-01-22 10:41:54 [scrapy.middleware] INFO: Enabled item pipelines:    
['myproject.pipelines.JSONPipline']
2020-01-22 10:41:54 [scrapy.core.engine] INFO: Spider opened
2020-01-22 10:41:54 [ptt_crawler] DEBUG: Start: open_spider ...
2020-01-22 10:41:54 [ptt_crawler] DEBUG: Create temp file for store JSON - E:\Code\dev-projects\Cupoy\pycrawler\myproject\crawled_data\.tmp.json.swp
2020-01-22 10:41:54 [ptt_crawler] DEBUG: End: open_spider ...
2020-01-22 10:41:54 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-01-22 10:41:54 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-01-22 10:41:55 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.ptt.cc/robots.txt> (referer: None)
2020-01-22 10:41:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html> (referer: None)
2020-01-22 10:41:55 [py.warnings] WARNING: E:\Code\dev-projects\Cupoy\pycrawler\myproject\myproject\spiders\ptt_crawler.py:32: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 32 of the file E:\Code\dev-projects\Cupoy\pycrawler\myproject\myproject\spiders\ptt_crawler.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.

  soup = BeautifulSoup(response.text)

2020-01-22 10:41:55 [ptt_crawler] DEBUG: Start: process_item ...
2020-01-22 10:41:55 [ptt_crawler] DEBUG: End: process_item ...
2020-01-22 10:41:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html>
{'id': 'M.1559788476.A.074', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html', 'author': 'STAV72 (刁民黨黨務主委)', 'title': '[問卦] 新疆爆發禽流感  
總撲殺數破萬', 'date': 'Thu Jun  6 10:34:34 2019', 'content': 'https://i.imgur.com/ZDkP38v.jpg https://i.imgur.com/rhToRIS.jpg 2019年5月30日，農業農村部接到動物疫病預
防控制中心報告，經國家禽流感參考實驗室\n確診，伊犁州霍爾果斯市部分養殖戶飼養的家禽發生H5N6亞型高致病性禽流感疫情。相\n關養殖戶共存欄家禽2445羽，發病1503羽，死亡1015余
羽。疫情發生後，當地按照有關\n預案和防治技術規範要求，切實做好疫情處置工作，已 撲殺家禽11910羽 ，全部病死和撲\n殺家禽均已無害化處理。\n\n\nSent from BePTT https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html 什麼時候可以貼港澳新聞了，\n只能爆卦啊？連新唐人跟大紀元都沒報，\n去哪生臺灣新聞？\n\n三明治也沒有，只能爆卦啊？', 'comments': [{'push_tag': '→', 'push_userid': 's820912gmail', 'push_content': '韓流', 'push_ipdatetime': '06/06 10:34'}, {'push_tag': '噓', 'push_userid': 'kent', 'push_content': '新聞改爆卦喔 我國三洨', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '→', 'push_userid': 'linceass', 'push_content': '沒牛雞吃了 只能吃豬', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '→', 'push_userid': 'Kreen', 'push_content': '讓中國人吃下肚消滅病原～', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '推', 'push_userid': 'dbdudsorj', 'push_content': '吃草吧', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '推', 'push_userid': 'mack860120', 'push_content': '習下韓上', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '噓', 'push_userid': 'no4', 'push_content': '', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '→', 'push_userid': 'linceass', 'push_content': '88你違反板龜了', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '推', 'push_userid': 'coollonger', 'push_content': '連鳥也沒得吃了嗎', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '→', 'push_userid': 'jorden', 'push_content': '豬雞都生病嘞 接下來換牛羊了 塊陶阿 天譴來了', 'push_ipdatetime': '06/06 10:35'}, {'push_tag': '噓', 'push_userid': 'pigpig1103', 'push_content': '這種事還要講？沒事啦幹', 'push_ipdatetime': '06/06 10:36'}, {'push_tag': '→', 'push_userid': 'henry55566', 'push_content': '韓流發威', 'push_ipdatetime': '06/06 10:36'}, {'push_tag': '推', 'push_userid': 'cores', 'push_content': '昨天是牛，今天換家禽，中國怎麼了，這
樣怎麼中或贏啦XD', 'push_ipdatetime': '06/06 10:37'}, {'push_tag': '推', 'push_userid': 'kyowinner', 'push_content': '人都可以撲殺了何況家禽', 'push_ipdatetime': '06/06 10:37'}, {'push_tag': '→', 'push_userid': 'echo3283', 'push_content': '中共可以吃吐吃草 怕什麼', 'push_ipdatetime': '06/06 10:38'}, {'push_tag': '→', 'push_userid': 'hbj1941', 'push_content': '整體可控，沒4', 'push_ipdatetime': '06/06 10:38'}, {'push_tag': '→', 'push_userid': 'Ipadhotwater', 'push_content': '這種爆發狀況中國的 
確是贏家', 'push_ipdatetime': '06/06 10:38'}, {'push_tag': '推', 'push_userid': 'bigbirdfly', 'push_content': '嚴重懷疑中共被投放病毒……怎麼這幾年狂得病', 'push_ipdatetime': '06/06 10:39'}, {'push_tag': '→', 'push_userid': 'beyoursky', 'push_content': '台灣如果對自己有信心 就不用怕引進中國雞肉', 'push_ipdatetime': '06/06 10:39'}, {'push_tag': '推', 'push_userid': 'xxxg00w0', 'push_content': '........豬 牛 接下來換雞鴨...剩羊了嗎= ="', 'push_ipdatetime': '06/06 10:40'}, {'push_tag': '噓', 'push_userid': 'kent', 'push_content': '我國是三洨啊', 'push_ipdatetime': '06/06 10:40'}, {'push_tag': '推', 'push_userid': 'color3258', 'push_content': '中國大煉蠱', 'push_ipdatetime': '06/06 10:40'}, {'push_tag': '→', 'push_userid': 'cores', 'push_content': '美國生物技術很強，貿易戰上要加大中國困局，是有動機的', 'push_ipdatetime': '06/06 10:40'}, {'push_tag': '推', 'push_userid': 'color3258', 'push_content': '中國有羊炭疽啊', 'push_ipdatetime': '06/06 10:42'}, {'push_tag': '→', 'push_userid': 'cores', 'push_content': '非洲豬瘟、秋行軍蟲、牛口蹄疫、羊碳疽、雞禽流感 很慘', 'push_ipdatetime': '06/06 10:43'}, {'push_tag': '噓', 'push_userid': 'yniori', 'push_content': '你的國家好爛喔~一直在死雞死牛死豬~~', 'push_ipdatetime': '06/06 10:43'}, {'push_tag': '→', 'push_userid': 'yniori', 'push_content': '但不管怎樣~都不會死超過35人
喔!!', 'push_ipdatetime': '06/06 10:43'}, {'push_tag': '→', 'push_userid': 'STAV72', 'push_content': '修一下好了，不然感覺到吵個沒完。', 'push_ipdatetime': '06/06 10:44'}, {'push_tag': '→', 'push_userid': 'yu1111116', 'push_content': '哇靠！ 這是在收集解成就喔', 'push_ipdatetime': '06/06 10:44'}, {'push_tag': '推', 'push_userid': 
'tamynumber1', 'push_content': '中國現在還有什麼傳染病還沒解鎖成就的?', 'push_ipdatetime': '06/06 10:47'}, {'push_tag': '推', 'push_userid': 'bbbyy', 'push_content': 
'阿六病死照吃 禽流感沒影響', 'push_ipdatetime': '06/06 10:58'}, {'push_tag': '推', 'push_userid': 'insist0511', 'push_content': '還有草能吃 沒事兒沒事兒', 'push_ipdatetime': '06/06 11:33'}], 'comment_stats': {'all': 32, 'count': 7, 'push': 12, 'boo': 5, 'neutral': 15}}
2020-01-22 10:41:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html> (referer: None)
2020-01-22 10:41:56 [ptt_crawler] DEBUG: Start: process_item ...
2020-01-22 10:41:56 [ptt_crawler] DEBUG: End: process_item ...
2020-01-22 10:41:56 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html>
{'id': 'M.1557928779.A.0C1', 'url': 'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html', 'author': 'hahaccu (靠臉吃飯的小魯)', 'title': '[問卦] 請家人吃飯好店 
推薦', 'date': 'Wed May 15 21:59:37 2019', 'content': '大家好，台嘎後，打給後\n\n本肥請家人吃飯\n\n每次只能想到欣葉，馬辣等吃到飽沒新意的店\n\n有沒有厲害有特色的店可 
以推薦\n\n謝謝\n\n https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html 對，北部 味道不是都一樣ㄇ (筆記)', 'comments': [{'push_tag': '→', 'push_userid': 'uuyouru', 'push_content': '住哪', 'push_ipdatetime': '05/15 21:59'}, {'push_tag': '噓', 'push_userid': 'DsLove710', 'push_content': '麥當勞', 'push_ipdatetime': '05/15 21:59'}, {'push_tag': '→', 'push_userid': 'uuyouru', 'push_content': '台北ㄇ', 'push_ipdatetime': '05/15 22:00'}, {'push_tag': '→', 'push_userid': 'hawaii987', 'push_content': '你家巷口', 'push_ipdatetime': '05/15 22:00'}, {'push_tag': '噓', 'push_userid': 'Doub1eK', 'push_content': '我家巷口', 'push_ipdatetime': '05/15 22:00'}, {'push_tag': '推', 'push_userid': 'pipi8696044', 'push_content': '台科大自助餐', 'push_ipdatetime': '05/15 22:00'}, {'push_tag': '→', 'push_userid': 'tyrande', 'push_content': 'M記快餐 K記快餐', 'push_ipdatetime': '05/15 22:00'}, {'push_tag': '→', 'push_userid': 'DongWooNeKo', 'push_content': '不知道', 'push_ipdatetime': '05/15 22:00'}, 
{'push_tag': '→', 'push_userid': 'JEWH', 'push_content': '女權', 'push_ipdatetime': '05/15 22:00'}, {'push_tag': '→', 'push_userid': 'guhong', 'push_content': '中壢家
樂福一樓的三商巧福，好吃到舌頭掉下來', 'push_ipdatetime': '05/15 22:01'}, {'push_tag': '→', 'push_userid': 'alex00089', 'push_content': '墾丁嗎？', 'push_ipdatetime': '05/15 22:04'}, {'push_tag': '推', 'push_userid': 'boboking2', 'push_content': '新馬辣', 'push_ipdatetime': '05/15 22:05'}], 'comment_stats': {'all': 12, 'count': 0, 'push': 2, 'boo': 2, 'neutral': 8}}
2020-01-22 10:41:56 [scrapy.core.engine] INFO: Closing spider (finished)
2020-01-22 10:41:56 [ptt_crawler] DEBUG: Start: close_spider ...
2020-01-22 10:41:56 [ptt_crawler] DEBUG: Save result at E:\Code\dev-projects\Cupoy\pycrawler\myproject\crawled_data\ptt-gossip.json
2020-01-22 10:41:56 [ptt_crawler] DEBUG: End: close_spider ...
2020-01-22 10:41:56 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 855,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 7569,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 1.310128,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 1, 22, 2, 41, 56, 35610),
 'item_scraped_count': 2,
 'log_count/DEBUG': 15,
 'log_count/INFO': 10,
 'log_count/WARNING': 1,
 'response_received_count': 3,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 1, 22, 2, 41, 54, 725482)}
2020-01-22 10:41:56 [scrapy.core.engine] INFO: Spider closed (finished)
```
