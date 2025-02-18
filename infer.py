from functools import cached_property
import os
import shutil
from expdataloader import *
from core.test_xportrait import XPortraitRunner


class XPortraitLoader(RowDataLoader):
    def __init__(self, name="XPortrait"):
        super().__init__(name)
        self.model = XPortraitRunner()

    @cached_property
    def model(self):
        return XPortraitRunner()

    def run_video(self, row):
        output_video_path = self.model.run(row.source_img_path, row.target_video_path, row.output_dir)
        shutil.copyfile(output_video_path, row.output_video_path)


def main():
    loader = XPortraitLoader()
    # loader.run_all()
    loader.test_20250218()


if __name__ == "__main__":
    main()
