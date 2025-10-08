from functools import cached_property
import os
import shutil
from expdataloader import *
from core.test_xportrait import XPortraitRunner


class XPortraitLoader(RowDataLoader):
    def __init__(self, name="XPortrait1", disable_fp16=False):
        super().__init__(name)
        self.disable_fp16 = disable_fp16
        self.model = XPortraitRunner(disable_fp16=disable_fp16)

    @cached_property
    def model(self):
        return XPortraitRunner(disable_fp16=self.disable_fp16)

    def run_video(self, row):
        output_video_path = self.model.run(row.source_img_path, row.target.video_path, row.output_dir)
        shutil.copyfile(output_video_path, row.output_video_path)

def test():
    model = XPortraitRunner()

def main():
    loader = XPortraitLoader(disable_fp16=True)
    loader.run_all()


if __name__ == "__main__":
    main()
