import os
import win32com.client
from win32com.client import constants, gencache
import xlrd

'''
应用场景：将word文件夹下存放的word文档，批量转换成pdf文件，并输出到pdf文件夹下
前提：本机安装了wps 2016或以上版本

'''
def ConvertDocToPdf(o,src, dst):
    if not os.path.exists(src):
        print(src + "不存在，无法继续！")
        return False
    if os.path.exists(dst):
        return
    
    o.Visible = False
    doc = o.Documents.Open(src)
    doc.ExportAsFixedFormat(dst, 17)
    doc.Close()
    if os.path.exists(dst):
        return True
    else:
        return False
basePath = 'word'
o = win32com.client.Dispatch("Kwps.Application")
for root, dirs, files in os.walk(basePath):
    for f in files:        
        print(os.path.abspath(os.path.join(root,f)))
        newFileName = os.path.splitext(os.path.basename(f))[0]+ '.pdf'    
        ConvertDocToPdf(o,os.path.abspath(os.path.join(root,f)) , os.path.abspath('pdf\\'+newFileName))
o.Quit()