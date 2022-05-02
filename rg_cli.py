#!/usr/bin/env python
import click
from pptx import Presentation


@click.option('--load', '-l', default=None, help='Load a presentation')
def load_slide():
    f = open('PyCon TW 2021 結案報告.pptx')
    try:
        prs = Presentation(f)
        print("load success")
    except Exception as error:
        print(error)
    f.close()

# @click.option
# def fill_in_slide_data():
#     fill("asdf.ppt")

if __name__ == '__main__':
    load_slide()



