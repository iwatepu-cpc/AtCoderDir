import AtCoderTasks

import os
import argparse

def fetch(url):
    task_urls = AtCoderTasks.get_task_urls(url)
    tasks = {key:AtCoderTasks.get_samples(turl) for key, turl in task_urls.items()}
    root = url.split('/')[-1]
    os.mkdir(root)
    for key, samples in tasks.items():
        path = root+'/'+str(key)+'/testcases'
        os.makedirs(path, exist_ok=True)
        for idx, sample in enumerate(samples, 1):
            with open(path+'/in'+str(idx)+'.txt', mode='w') as f:
                f.write(sample[0])
            with open(path+'/out'+str(idx)+'.txt', mode='w') as f:
                f.write(sample[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch AtCoder problem tasks.')
    parser.add_argument('url', help='https://atcoder.jp/contests/*', type=str)
    args = parser.parse_args()
    if args.url:
        fetch(args.url)
    else:
        parser.print_usage()
