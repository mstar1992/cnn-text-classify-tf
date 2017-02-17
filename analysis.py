# encoding=utf-8
import codecs
import re,os
PATH = 'data'
INTENT_PATH = 'data/intent'
# INTENT_PATH = '../dockerData/rachel/cnn-text-classify-tf/data/intent'
PREDICT_PATH = 'runs/1481471864'
def analysis():
    dic_label ={}
    dic_predict={}
    with codecs.open(os.path.join(PATH, 'mongodata_2016120901.txt'), 'r', 'utf-8') as f:
        for line in f.readlines():
            # print type(line)
            label = line.strip().split('   ')[0]
            content = line.strip().split('   ')[1].encode('utf-8')
            if label=='1':
                label = '0.0'.encode('utf-8')
            else:
                label = '1.0'.encode('utf-8')
            # print type(content)
            dic_label[content] = label
    with codecs.open(os.path.join(PREDICT_PATH, 'prediction.csv'), 'r', 'utf-8') as f:
        for line in f.readlines():
            label = line.strip().split(',')[1]
            # print label,type(label)
            content = line.strip().split(',')[0]
            dic_predict[content] = label
    pos_neg = ['pos is labeled wrongly as neg']
    neg_pos = ['neg is labeled wrongly as pos']
    for k,v in dic_label.items():
        decode_k = k.decode('utf-8')
        try:
            if dic_label[k]!=dic_predict[decode_k]:
                if dic_label[k] == '1.0':
                    pos_neg.append(k)
                else:
                    neg_pos.append(k)
        except Exception as e:
            print e
    with codecs.open(os.path.join(INTENT_PATH, 'error_20161211.txt'), 'a', 'utf-8') as f:
        for i in pos_neg:
            f.write(i.decode('utf-8'))
            f.write('\n')
        for i in neg_pos:
            f.write(i.decode('utf-8'))
            f.write('\n')
if __name__ == "__main__":
    analysis()