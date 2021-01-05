'''
应用场景：将一个文本文件拆分为多份，例如：有时候一次不宜执行太多条sql语句，则可使用此脚本拆分为多份
'''

with open("files/demo.txt") as f:
    lines = f.readlines()
    totalCount = len(lines)
    currIndex = 1

    currPage = 1;
    tempStr = ''
    pageCount = 10000
    for line in lines:
        tempStr = tempStr + line
        if currIndex % pageCount == 0 or currIndex == totalCount :
            fileResult = open('files/demo-{0}.txt'.format(str(currPage)), 'a+')
            fileResult.write(tempStr)
            fileResult.close()
            tempStr = ''
            currPage = currPage + 1;
        currIndex = currIndex + 1
