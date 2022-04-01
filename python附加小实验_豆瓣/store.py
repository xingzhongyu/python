import requests  
import time
from selenium import webdriver 
from wordcloud import WordCloud
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from io import BytesIO
from PIL import Image
import helppdf
from bs4 import BeautifulSoup

# headers = {'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'}  
# r = requests.get('http://www.xinhuanet.com/politics/2020-12/29/c_1126919544.htm' , headers = headers) 
# r.encoding = r.apparent_encoding
# bs = BeautifulSoup(r.text , "lxml")
# from selenium import webdriver
testPic=True
movies=[]
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
def opens(driver):
    time.sleep(1)
    store(driver)
    time.sleep(3)
    target=driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div[2]/span[3]/a")
    driver.execute_script("arguments[0].scrollIntoView();",target)
    time.sleep(1)
    act=ActionChains(driver).click(target)
    act.perform()
    time.sleep(1)
    global testPic
    if(testPic==True):
        testPic=False
        for movie in movies:
            p=requests.get(movie["img_url"])
            byte_stream=BytesIO(p.content)
            im=Image.open(byte_stream)
            if im.mode=="RGBA":
                im.load()
                background=Image.new("RGB",im.size(),(255,255,255))
                background.paste(im,mask=im.split()[3])
            im.save("./sources/pics/"+movie["title"]+'.jpg','JPEG')
            # with open("D:/python/test002/sources/pics/"+movie["title"]+'.webp','wb') as f:
            #     f.write(im)
            #     f.close()
def store(driver):
    i=1
    while(True):
        try:
            img_url=driver.find_element_by_xpath("//*[@id='content']/div/div[1]/ol/li["+str(i)+"]/div/div[1]/a/img").get_attribute("src")
            title=driver.find_element_by_xpath("//*[@id='content']/div/div[1]/ol/li["+str(i)+"]/div/div[2]/div[1]/a/span[1]").text
            score=driver.find_element_by_xpath("//*[@id='content']/div/div[1]/ol/li["+str(i)+"]/div/div[2]/div[2]/div/span[2]").text
            infor=driver.find_element_by_xpath("//*[@id='content']/div/div[1]/ol/li["+str(i)+"]/div/div[2]/div[2]/p[1]").text 
            # print("title="+title)
            # print("score="+score)
            # print("img_url="+img_url)
            infs=str(str(infor).split(sep="\n")[1]).split(sep="/")
            # print("year="+infs[0])
            # print("nation="+infs[1])
            # print("category="+infs[2])
            movie={"title":title,"score":score,"img_url":img_url,"year":infs[-3].strip(),"nation":infs[-2].strip(),"category":infs[-1].strip()}
            movies.append(movie)
            i+=1
        except:
            break
        

if __name__=="__main__":
    driver = webdriver.Chrome("./chromeDriver/chromedriver.exe")    # 这里会打开chrome注意是91版
    driver.get(r"https://movie.douban.com/top250") # 打开url网页 比如 driver.get("")
    for i in range(1,10):
        opens(driver)
    store(driver)
    time.sleep(5)
    print(movies)
    movies=pd.DataFrame(data=movies)
    movies.to_csv(path_or_buf="./movies.csv",encoding="gb18030")
    print("finish")
    helppdf.makePdf("图片总览.pdf","./sources/pics")
    driver.close()
    


