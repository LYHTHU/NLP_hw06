import os

class FeatureBuilder:
    def __init__(self, input_path = "./CONLL_train.pos-chunk-name", train_mode = True):
        self.out_path = input_path[input_path.rfind("/")+1: input_path.rfind(".")] + ".feature"
        self.in_file = open(input_path, 'r')
        self.out_file = open(self.out_path, 'w')
        self.train_mode = train_mode

    @staticmethod
    def exec_line(line):
        for i in range(0, 32):
            line = line.replace(chr(i), " ")
        line = line.strip().split(" ")
        return tuple(i for i in line)

    def append_feature(self, token, feature, tag):
        str = token
        for f in feature:
            str = str + "\t" + "feature=" + f
        if self.train_mode:
            str = str + "\t" + tag
        str = str + "\n"
        self.out_file.write(str)

    def close_file(self):
        self.in_file.close()
        self.out_file.close()

    def exec_sentence(self, sentence):
        length = len(sentence)

        for i, data in enumerate(sentence):
            if self.train_mode:
                token, pos, bio, tag = data[0], data[1], data[2], data[3]
            else:
                token, pos, bio = data[0], data[1], data[2]

            if i > 0:
                pre = sentence[i - 1]
            else:
                pre = (None, "start", 0, 0)
            if i < length - 1:
                post = sentence[i + 1]
            else:
                post = (None, "end", 0, 0)

            feature = (pos, pre[1], post[1])

            if token == "-DOCSTART-":
                feature = ("0", "0", "0")

            if self.train_mode:
                self.append_feature(token, feature, tag)
            else:
                self.append_feature(token, feature, None)

        self.out_file.write("\n")

    def run(self):
        sentence = []
        count = 0
        while True:
            line = self.in_file.readline()
            if not line:
                break
            data = self.exec_line(line)
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
    dev_feature = "CONLL_dev.feature"
    dev_out = "response.name"
    os.system("java -cp .:./maxent-3.0.0.jar:trove.jar MEtrain " + builder.out_path + " " + model_name)

    builder = FeatureBuilder(input_path=dev_name, train_mode=False)
    builder.run()

    os.system("java -cp .:./maxent-3.0.0.jar:trove.jar MEtag " + dev_feature + " " + model_name + " " + dev_out)
    os.system("python3 score.name.py")
