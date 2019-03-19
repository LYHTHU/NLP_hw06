class FeatureBuilder:
    def __init__(self, input_path = "./CONLL_train.pos-chunk-name"):
        out_path = input_path
        out_path = out_path[out_path.rfind("/")+1 : out_path.rfind(".") + ".name"]

    def exec_line(self, line):
        pass

    def append_feature(self, feature):
        pass

    def close_file(self):
        pass

