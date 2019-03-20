import os

class FeatureBuilder:
    def __init__(self, input_path = "./CONLL_train.pos-chunk-name"):
        out_path = input_path
        out_path = out_path[out_path.rfind("/")+1 : out_path.rfind(".")] + ".name"
        print("Output:", out_path)
        self.in_file = open(input_path, 'r')
        self.out_file = open(out_path, 'w')

    @staticmethod
    def exec_line(line):
        for i in range(0, 32):
            line = line.replace(chr(i), " ")
        line = line.strip().split(" ")
        return tuple(i for i in line)

    def append_feature(self, feature):
        pass

    def close_file(self):
        self.in_file.close()
        self.out_file.close()

    def run(self):
        sentence = []
        count = 0
        while True:
            line = self.in_file.readline()
            if not line:
                break
            data = self.exec_line(line)
            if data[0] == "-DOCSTART-":
                # skip the first 2 lines
                self.in_file.readline()
                continue
            sentence.append(data)
            if len(data) == 1:
                count += 1
                # print(count, "->sentence = ", sentence)
                sentence = []

        print("Finished.")
        self.close_file()

        print("There is ", count, "sentences in training file.")


if __name__ == '__main__':
    builder = FeatureBuilder()
    builder.run()

    os.system("rm *.class")
    os.system("javac -cp ./maxent-3.0.0.jar:trove.jar ./*.java")
