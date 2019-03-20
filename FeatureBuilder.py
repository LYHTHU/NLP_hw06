import os

class FeatureBuilder:
    def __init__(self, input_path = "./CONLL_train.pos-chunk-name", train_mode = True):
        self.out_path = input_path[input_path.rfind("/")+1: input_path.rfind(".")] + ".feature"
        self.in_file = open(input_path, 'r')
        self.out_file = open(self.out_path, 'w')

    @staticmethod
    def exec_line(line):
        for i in range(0, 32):
            line = line.replace(chr(i), " ")
        line = line.strip().split(" ")
        return tuple(i for i in line)

    def append_feature(self, token, feature):
        str = token
        for f in feature:
            str = str + "\t" + "feature=" + f
        str = str + "\n"
        self.out_file.write(str)

    def append_feature(self, token, feature, tag):
        str = token
        for f in feature:
            str = str + "\t" + "feature=" + f
        str = str + "\t" + tag + "\n"
        self.out_file.write(str)

    def close_file(self):
        self.in_file.close()
        self.out_file.close()

    def exec_sentence(self, sentence):
        for i, data in enumerate(sentence):
            token, pos, bio, tag = data[0], data[1], data[2], data[3]
            if i > 0:
                pre = sentence[i - 1]
                feature = (pos, pre[1])
                self.append_feature(token, feature, tag)
            else:
                feature = (pos, "start")
                self.append_feature(token, feature, tag)

    def run(self):
        sentence = []
        count = 0
        while True:
            line = self.in_file.readline()
            if not line:
                break
            data = self.exec_line(line)
            if data[0] == "-DOCSTART-":
                self.in_file.readline()
                continue

            sentence.append(data)
            if len(data) == 1:
                count += 1
                sentence.pop()
                self.exec_sentence(sentence)
                sentence = []

        print("Finished.")
        print("Output:", self.out_path)
        self.close_file()

        print("There is ", count, "sentences in training file.")


if __name__ == '__main__':
    builder = FeatureBuilder(train_mode=True)
    builder.run()

    if not (os.path.exists("MEtrain.class") and os.path.exists("MEtag.class")):
        os.system("javac -cp ./maxent-3.0.0.jar:trove.jar ./*.java")

    model_name = "MEmodel.bin.gz"
    dev_name = "CONLL_dev.pos-chunk"
    dev_out = "response.name"
    os.system("java -cp .:./maxent-3.0.0.jar:trove.jar MEtrain " + builder.out_path + " " + model_name)
    os.system("java -cp .:./maxent-3.0.0.jar:trove.jar MEtag " + dev_name + " " + model_name + " " + dev_out)
    os.system("python3 score.name.py")
