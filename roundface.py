import os
import cv2
import numpy as np


class RoundFace:
    def __init__(self, source, output_size, is_greyed):
        base_dir = os.path.dirname(__file__)
        prototxt_path = os.path.join(base_dir + 'model/deploy.prototxt')
        caffemodel_path = os.path.join(base_dir + 'model/weights.caffemodel')

        self.base_dir = base_dir
        self.image_source = self.validate_image_source(source)
        self.output_size = output_size
        self.is_greyed = bool(is_greyed)
        self.source_is_file = os.path.isfile(self.image_source)  
        self.dest_dir = self.create_dest_dir()

        self.model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    def process(self):
        if not self.source_is_file:
            self.process_folder()
        else:
            self.process_file(self.image_source)


    def process_folder(self):
        pass

    def process_file(self, filepath):
        pass

    def validate_image_source(self, image_path):
        validated_path = ''
        working_dir = os.getcwd()
        relative_path = os.path.join(working_dir,image_path)

        if os.path.exists(relative_path):
            validated_path = relative_path
        
        else:
            if not os.path.exists(image_path):
                raise Exception("Invalid Image Source")
        
        return validated_path

    def create_dest_dir(self):
        source_parent = os.path.dirname(self.image_source)
        dest_dir = os.path.join(source_parent,"roundface")

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        return dest_dir



parser = argparse.ArgumentParser()
parser.add_argument('-s','--source', required=True,
                    help="Image Source. It can be a file or folder")

parser.add_argument('-g','--grey', type=int, default=0,
    help="Whether resulting photos should be greyed out. 0 for False, 1 for True.")

parser.add_argument('-sz','--size', type=int,
    help="Number. Output size in pixels.")
args = parser.parse_args()

rf = RoundFace(args.source, args.size, args.grey)
rf.process()
