import jieba
choice = int(input('输入1分词\n输入2提取关键词\n'))
if choice==1:
    # 交互式输入
    dict = input('请输入字典dict路径: ')
    jieba.load_userdict(dict)
    # 预设
    # jieba.load_userdict("D:\\Programming\\Python\\Python_Programs\\Luxun\\file\\dict.txt")
    file = input('请输入待处理文件路径: ')
    lines = open(file,encoding='utf8').read()
    new = input('请输入新文件路径: ')
    newfile = open(new,"w",encoding= 'utf8')
    seg_list = jieba.cut(lines)
    newfile.write(" ".join(seg_list))
    newfile.close()
elif choice==2:
    import jieba.analyse as analyse
    # 交互式输入
    stop = input('请输入忽略stop路径: ')
    jieba.nalyse.set_stop_words(stop)
    # 预设
    # jieba.analyse.set_stop_words('D:\\Programming\\Python\\Python_Programs\\Luxun\\file\\stop.txt')
    file = input('请输入待处理文件路径: ')
    lines = open(file,encoding= 'utf8').read()
    new = input('请输入新文件路径: ')
    newfile = open(new,"w",encoding= 'utf8')
    num=int(input('请输入高频词个数: '))
    newfile.write("  ".join(analyse.extract_tags(lines, topK=num, withWeight=False, allowPOS=())))
    newfile.close()
else:
    print('错误输入')
