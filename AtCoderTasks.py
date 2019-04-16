import requests
import bs4

__atcoder__ = 'https://atcoder.jp'

def get_task_urls(base_url):
    url = base_url+'/tasks'
    q = requests.get(url)
    html = bs4.BeautifulSoup(q.text, 'html.parser')
    links = html.select('td.text-center > a')
    return {l.text:__atcoder__+l.attrs['href'] for l in links}

def get_samples(url):
    q = requests.get(url)
    html = bs4.BeautifulSoup(q.text, 'html.parser')
    samples = []
    for i in range(1, 30):
        isample = html.find(string='入力例 '+str(i))
        if isample is None:
            break
        osample = html.find(string='出力例 '+str(i))
        samples.append((isample.parent.next_sibling.text.replace('\r', ''), osample.parent.next_sibling.text.replace('\r', '')))
    return samples
