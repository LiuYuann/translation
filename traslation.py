import urllib.request
import urllib.parse
import json
import easygui as g
content=""
while(content!='.'):
    content = g.enterbox("请输入","元哥牌词典")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
    data = {}
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    data['i'] = content
    data['from'] = 'AUTO'
    data['to']='Auto'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='1521687034344'
    data['sign']='8b0f22fd8ff58a776255e726fd0239ef'
    data['doctype']= 'json'
    data['version']='2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_REALTIME'
    data['typoResult']= 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req=urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    g.msgbox("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
