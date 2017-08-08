#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/8
# Title:
# Tip:
import docx
from app.models import Topic


def importDefaultTopic():
    topicModel = Topic()
    path = "file/zhenX.docx"
    doc = docx.Document(path)
    paras = doc.paragraphs
    parastests = [p.text for p in paras if p.text.isspace() is False]
    for content in parastests:
        topic_list = content.split("\n")
        for topic in topic_list:
            topic = topic.strip()
            if topic.isspace() is False and topic != '':
                try:
                    topic_arr = topic.strip().split(".")
                    if topic_arr and len(topic_arr) > 0:
                        topicModel.addNewTopic(topic_arr[1])
                        pass
                    pass
                except Exception as err:
                    print err.message
                    print "wrong:" + topic.strip()
                    pass
    pass



if __name__ == '__main__':

    pass