# Split_or_Count_Chinese_Words
> 个人学习Python的一个小任务  
程序运用'jieba'和文件操作将txt文章分作词语或统计自定义个数高频词。  

## 使用
用Cpython解释器运行，根据窗口提示选择功能，然后输入字典地址、停用字典地址、待处理文件地址、新文件地址和高频词个数，稍等片刻或~~久的一笔~~，可得到分词或高频词结果。

## 注意事项
- 地址输入时'\\'请输入为转义符'\\\\'。
- 地址输入记得包含完整文件名，如"D:\\\\dict.**txt**""，否则将无法找到待处理文件或创建无后缀名新文件。
- 字典和停用字典均可为空，此时分词程序将使用默认字典，统计高频词程序不对高频词执行任何操作。
- 字典每行格式为"词1 1000"，一行一词。使用自定义字典不是完全替换默认字典，而是优先遵循自定义字典分词。所以实际使用可以先用默认字典分词，然后利用自定义字典微调优化。
- 停用字典每行格式为"词"，一行一词。使用自定义停用字典即忽略一部分词，后续词替代，仍将生成自定义个数个词。
