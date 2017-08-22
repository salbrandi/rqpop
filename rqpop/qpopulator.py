# -*- coding: utf-8 -*-
# ------------------- #
# Third Party Imports #
# ------------------- #
import click
from stressypy import JobBlock,
                      cpustresser.create_job  as create_job,
                      get_time_used
from redis import Redis
from rq import Queue
import multiprocessing as mp
import time
import random
from scipy import numpy.random as rdm

# ------------------- #
#    Local Imports    #
# ------------------- #
# None

redis_conn = Redis()
q = Queue(connection=redis_conn)

class BlockBox:

    total_boxes = 0

    def __init__(self, block_list, boxid):
        self.blocks = block_list
        self.id = boxid
        total_boxes = len(block_list)

    def add_block(self, block):
        self.blocks.append(block)
        BlockBox.total_boxes += 1

    def remove_block(self, block):
        self.blocks.remove(block)
        BlockBox.total_boxes += 1

def generate_test_jobs(job_count, max_time, min_time=1, min_cpu=1, max_cpu=mp.cpu_count, distribution='normal', seed=None):

    seed = rdm.seed(seed=seed)

    if distribution is 'normal':
        random_cpu = rdm.lognormal(min_cpu, 1, max_cpu)
        random_time = int(rdm.lognormal(min_time, 1, max_time)
    else if distribution is 'spike':
        pass


    block_lst = []
    for i, num in enumerate(range(job_count)):
        job = create_job(random_cpu, random_time)
        block_lst.append(job)
    box = BlockBox.new(block_lst, 1)

    for block in box.blocks:
        q.enqueue(block.func, *block.func_args, **block.func_kwargs)

    print(box.blocks)
    return {'box':box }


num_tests = 0;
