#!/usr/bin/env python
import click


@click.command()
@click.argument("slide_template")
def load_slide(slide_template):
    click.echo(slide_template)

if __name__ == '__main__':
    load_slide()
