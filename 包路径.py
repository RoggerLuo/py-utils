(问题：使用相对路径，是相对 使用这个包的文件的路径，结果找不到资源）
想要引用自己包内的资源，使用
    db_path = os.path.dirname(os.path.realpath(__file__))+'/w2v.pkl'
来解决路径上的问题，
