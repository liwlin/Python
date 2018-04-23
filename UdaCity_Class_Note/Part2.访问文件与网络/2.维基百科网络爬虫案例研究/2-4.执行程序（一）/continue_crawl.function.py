 ###
 # @Author: Robot.LI 
 # @Date: 2018-04-09 16:00:48 
 # @Last Modified by:   Robot.LI 
 # @Last Modified time: 2018-04-09 16:00:48 
 # ctrl+alt+i
 ### 

'''
测验：continue_crawl 函数
我们需要编写的第一个帮助函数是 continue_crawl，其将用于我们的 while 循环，如下所示：

while continue_crawl(search_history, target_url):
例如，我们可以使用这些值调用函数：

continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
                       'https://en.wikipedia.org/wiki/Philosophy')
search_history 是维基百科文章 url 的字符串列表。列表中的最后一个项目是最近发现的 url。
如果 target_url 是查找到结果，停止搜索时文章 url 的字符串。
根据以下规则，continue_crawl 应该返回 True 或 False： 如果 search_history 中最近的文章是目标文章，则应停止搜索，
函数应返回 False 如果列表中有 25 个 url，函数应返回 False 如果列表中有一个循环，函数应返回 False 否则应继续搜索，
函数应返回 True。

对于该测验，执行 continue_crawl。对于停止搜索的每种情况，请打印一个简要说明原因的消息。 务必测试你的代码！


# TODO: Implement the continue_crawl function described above 
'''
def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:  # 如果最近的文章是目标文章，停止搜索，返回false
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:  #如果文章列表有超过25个连接，返回false
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]: #如果文章列表里面有重复的文章，返回false
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True  #都不满足以上情况，返回True，代表这是一个新的文章连接

print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'))

