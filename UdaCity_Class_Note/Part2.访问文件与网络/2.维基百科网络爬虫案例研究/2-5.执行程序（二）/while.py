###
#  # @Author: Robot.LI 
# @Date: 2018-04-12 10:58:04 
# @Last Modified by:   Robot.LI 
# @Last Modified time: 2018-04-12 10:58:04 
### 

'''
这四个步骤可作为 while 循环构架中的注释。

while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    # add the first link to article_chain
    # delay for about two seconds
现在可以执行一些操作。

第一步，在 article_chain 中下载最后一篇文章的 html 是我们将使用请求包从维基百科获取 html 的命令。
第二步，查找该 html 中的第一个链接 将涉及使用 BeautifulSoup 解析该 html，以获取第一个链接的 URL。
我建议将这两个步骤合并成一个单一的函数，其输入将是包含维基百科文章 URL 的字符串，
输出将是包含维基百科文章正文中第一个链接的 URL 的字符串。我们调用此函数 find_first_link。

步骤： 在 article_chain 中下载最后一篇文章的 html 与 查找该 html 中的第一个链接 是我们计划中最初的前两个步骤，
但将它们放在一个帮助函数 find_first_link 中，可使用外部库请求和 while 循环之外的 BeautifulSoup 提取全部详细信息。
这样做也很有用，原因是如果将来关于这些库工作原理的详细信息发生变化，我们仍然可以保留主 while 循环，而且只需更改帮助函数。
这也有助于保持代码真正可读性。

因为已经适当地定义了 find_first_link 的输入和输出，所以我可以把这个函数留给 Philip 执行 - 之后他将开始处理。
现在，我可以根据这个函数的输出内容，并通过将 find_first_link 调用到 while 循环中来使其发挥作用。

while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article chain
    # delay for about two seconds
索引 [-1] 提供了 article_chain 列表中的最后一个条目，所以在下一行，
将 first_link 添加到 article_chain 的末尾可起到一定作用 - 下一步将编写该代码！"

测验：将链接添加到文章链
写一行将 first_link 添加到 article_chain 列表末尾的代码。此行代码将位于注释 "将第一个链接添加到文章链" 之后。


'''




while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    # add the first link to article_chain
    # delay for about two seconds