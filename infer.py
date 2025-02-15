from expdataloader import *
from core.test_xportrait import XPortraitRunner

class XPortraitLoader(HeadGenLoader):
    def __init__(self, name="XPortrait"):
        super().__init__(name)
        self.model = XPortraitRunner()
        
    def run_video(self, row):
        out_imgs_dir = get_sub_dir(row.output_dir, "ori_output")
        self.model.run(row.source_img_path, row.target_video_path, out_imgs_dir)
    
def main():
    loader = XPortraitLoader()
    loader.run_test()
    
if __name__ == '__main__':
    main()