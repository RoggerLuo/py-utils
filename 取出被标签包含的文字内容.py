如果我有一百段如下类似的html代码，内部的标签还不固定，又如何使用xpath表达式，以最快最方便的方式提取出来？


<div id="test3">我左青龙，<span id="tiger">右白虎，<ul>上朱雀，<li>下玄武。</li></ul>老牛在当中，</span>龙头在胸口。<div>
data = selector.xpath('//div[@id="test3"]')
 info = data.xpath('string(.)').extract()[0]