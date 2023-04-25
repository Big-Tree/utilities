import subprocess as sp
import os


def get_gpu_mem_usage():
    command = "nvidia-smi --query-gpu=memory.used --format=csv"
    try:
        memory_free_info = sp.check_output(command.split()).decode('ascii').split('\n')[:-1][1:]
    except:
        print('nvidia-smi command failed')
        return -1
    memory_free_values = [int(x.split()[0]) for i, x in enumerate(memory_free_info)]

    if 'CUDA_VISIBLE_DEVICES' in os.environ:
        gpu_num = int(os.environ['CUDA_VISIBLE_DEVICES'])
    else:
        gpu_num = 0
    return memory_free_values[gpu_num]
