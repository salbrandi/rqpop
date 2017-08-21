# -*- coding: utf-8 -*-
# ------------------- #
# Third Party Imports #
# ------------------- #
import click
import stressypy


# ------------------- #
#    Local Imports    #
# ------------------- #


@click.group()
def rqpop():
    pass

@click.command()
@click.argument('num_jobs')
@click.option('--seed', default=1)
@click.option('--distribution', default='log normal')
def queue_loads(num_jobs, seed, distribution):
    pass

rqpop.add_command(queue_loads, name='queue')

if __name__ == '__main__':
    pass