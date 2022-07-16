from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        #实体识别和问题分类，该部分完成数据的提取和导入
        self.classifier = QuestionClassifier()
        #针对特定问题的查询
        self.parser = QuestionPaser()
        #回答语句的构建
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '抱歉，或许是数据库还未收纳您想要查询的信息，请尝试重新输入'

        #返回的是实体及其类别，以及问题类型
        res_classify = self.classifier.classify(sent)
        if  res_classify=='':
            print(answer)

        #print('类别：',res_classify)

        #返回的是问题类型和对应的查询结果
        res_sql = self.parser.parser_main(res_classify)
        #print('sql语句',res_sql)

        final_answers = self.searcher.search_main(res_sql)
        if final_answers=='':
            print(answer)

            #return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    #测试
    problems=["卧虎藏龙和花样年华的评分",
              "饮食男女的上映时间",
              "霸王别姬这部电影的风格"]
    for id,problem in enumerate(problems):
        print("第{0}个问题是{1}：".format(id+1,problem))
        handler.chat_main(problem)
        print("\n")
    print("测试结束")
    #测试-end
    while 1:
        question = input('咨询:')
        handler.chat_main(question)



