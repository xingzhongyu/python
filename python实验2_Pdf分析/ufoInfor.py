import jieba
from wordcloud import WordCloud
f=open('D:/python/test004/sources/ufoInformation.txt',encoding='utf-8')
txt=""
for line in f:
    txt=txt+line.strip()
words = jieba.lcut(txt)                                        #精确分词
newtxt = ' '.join(words)                                       #空格拼接
wordcloud = WordCloud(font_path="msyh.ttc").generate(newtxt)   #生成词云，font_path="msyh.ttc"为选择微软雅黑字体
image = wordcloud.to_image()
image.show()